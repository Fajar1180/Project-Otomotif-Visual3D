"""3D mesh generation engine adapter (Issue #5).

Supports multiple backends via ``THREE_D_ENGINE`` env var:

* ``fallback`` (default) — deterministic local generator that writes a valid
  ``.glb`` file to ``THREE_D_OUTPUT_DIR``. No PyTorch/InstantMesh weights,
  no GPU, no heavy download. Safe for dev / CI / local testing.
* ``replicate`` — POST to Replicate API (``REPLICATE_API_TOKEN`` +
  ``REPLICATE_MODEL_VERSION``).
* ``huggingface`` — POST to HuggingFace Inference API
  (``HUGGINGFACE_API_TOKEN`` + ``HUGGINGFACE_MODEL_ID``).
* ``external`` — POST to ``EXTERNAL_3D_WORKER_URL`` (GPU worker cluster).

Every adapter returns ``(mesh_url: str, texture_url: str | None)`` so the
Celery task never needs to know which engine is behind it.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import struct
import time
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from typing import Optional, Tuple

from config import settings

OUTPUT_DIR = settings.THREE_D_OUTPUT_DIR


class ThreeDEngineError(RuntimeError):
    """Raised when the 3D engine fails after all retries are exhausted."""


class ThreeDEngineAdapter(ABC):
    """Strategy interface: synthesize a mesh from 4 input image paths/URLs."""

    @abstractmethod
    def synthesize(self, image_urls: list[str]) -> Tuple[str, Optional[str]]:
        """Return ``(mesh_url, texture_url)`` or raise :class:`ThreeDEngineError`."""


# ---------------------------------------------------------------------------
# Fallback engine — deterministic .glb generator (no external deps)
# ---------------------------------------------------------------------------


class FallbackThreeDEngine(ThreeDEngineAdapter):
    """Generates a minimal but *valid* GLB file locally.

    The GLB contains a single white cube — enough to prove the
    ``/api/v1/3d/generate`` → Celery → ``/status`` contract end-to-end in
    environments without a GPU or model weights.
    """

    # Minimal glTF 2.0 JSON: one scene, one node, one mesh (box).
    _GLTF = {
        "asset": {"version": "2.0", "generator": "otomotif-ai-fallback"},
        "scene": 0,
        "scenes": [{"nodes": [0]}],
        "nodes": [{"mesh": 0}],
        "meshes": [
            {
                "primitives": [
                    {
                        "attributes": {"POSITION": 0},
                        "indices": 1,
                        "material": 0,
                        "mode": 4,  # TRIANGLES
                    }
                ]
            }
        ],
        "accessors": [
            {
                "bufferView": 0,
                "componentType": 5126,  # FLOAT
                "count": 8,
                "type": "VEC3",
                "max": [1, 1, 1],
                "min": [-1, -1, -1],
            },
            {
                "bufferView": 1,
                "componentType": 5123,  # UNSIGNED_SHORT
                "count": 36,
                "type": "SCALAR",
            },
        ],
        "bufferViews": [
            {"buffer": 0, "byteLength": 0, "byteStride": 12},  # filled below
            {"buffer": 0, "byteLength": 0},  # filled below
        ],
        "buffers": [{"byteLength": 0}],  # filled below
        "materials": [
            {
                "pbrMetallicRoughness": {
                    "baseColorFactor": [0.8, 0.8, 0.8, 1.0],
                }
            }
        ],
    }

    def synthesize(self, image_urls: list[str]) -> Tuple[str, Optional[str]]:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        # Short stable hash — base64 of full paths could blow past Windows
        # MAX_PATH once four absolute paths are involved.
        mesh_id = hashlib.sha256(
            json.dumps(sorted(image_urls)).encode()
        ).hexdigest()[:16]
        mesh_path = os.path.join(OUTPUT_DIR, f"{mesh_id}.glb")
        if os.path.exists(mesh_path):
            return f"/static/meshes/{os.path.basename(mesh_path)}", None

        # Build GLB: header + JSON chunk + BIN chunk.
        positions = b"".join(
            struct.pack("<fff", *v)
            for v in [
                (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
            ]
        )
        indices = b"".join(
            struct.pack("<H", i)
            for i in [
                0, 1, 2, 0, 2, 3,      # -z face
                4, 5, 6, 4, 6, 7,      # +z face
                0, 4, 5, 0, 5, 1,      # -y face
                2, 3, 7, 2, 7, 6,      # +y face
                0, 3, 7, 0, 7, 4,      # -x face
                1, 5, 6, 1, 6, 2,      # +x face
            ]
        )

        # Pad JSON chunk to 4-byte alignment.
        gltf_json = json.dumps(self._GLTF, separators=(",", ":")).encode()
        while (len(gltf_json) % 4) != 0:
            gltf_json += b" "

        json_chunk = struct.pack("<I", len(gltf_json)) + b"JSON" + gltf_json
        bin_chunk = struct.pack("<I", len(positions) + len(indices)) + b"BIN" + positions + indices

        header = struct.pack("<III", 0x46546C66, 2, 0)  # magic, version, length
        length = 12 + len(json_chunk) + len(bin_chunk)
        header = struct.pack("<III", 0x46546C66, 2, length)

        with open(mesh_path, "wb") as f:
            f.write(header)
            f.write(json_chunk)
            f.write(bin_chunk)

        # Browser needs a URL, not a filesystem path. main.py mounts
        # THREE_D_OUTPUT_DIR at /static/meshes.
        return f"/static/meshes/{os.path.basename(mesh_path)}", None


# ---------------------------------------------------------------------------
# Remote engines — Replicate, HuggingFace, external worker
# ---------------------------------------------------------------------------


class _RemoteThreeDEngine(ThreeDEngineAdapter):
    """Base for HTTP-backed engines (Replicate / HF / external)."""

    def __init__(self, endpoint: str, headers: dict[str, str], model_ref: str) -> None:
        self._endpoint = endpoint
        self._headers = headers
        self._model_ref = model_ref

    def _post(self, payload: dict) -> dict:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self._endpoint,
            data=data,
            headers={**self._headers, "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
        except urllib.error.HTTPError as exc:  # pragma: no cover - network
            body = exc.read()
            raise ThreeDEngineError(f"engine HTTP {exc.code}: {body!r}") from exc
        except urllib.error.URLError as exc:  # pragma: no cover - network
            raise ThreeDEngineError(f"engine unreachable: {exc}") from exc
        return json.loads(body.decode("utf-8") if body else "{}")

    @abstractmethod
    def synthesize(self, image_urls: list[str]) -> Tuple[str, Optional[str]]:
        ...


class ReplicateThreeDEngine(_RemoteThreeDEngine):
    """Replicate API adapter."""

    def __init__(self) -> None:
        super().__init__(
            endpoint="https://api.replicate.com/v1/predictions",
            headers={"Authorization": f"Token {settings.REPLICATE_API_TOKEN}"},
            model_ref=settings.REPLICATE_MODEL_VERSION,
        )

    def synthesize(self, image_urls: list[str]) -> Tuple[str, Optional[str]]:
        body = self._post(
            {
                "version": self._model_ref,
                "input": {"images": image_urls},
            }
        )
        # Poll until completion (Replicate returns a URL to poll).
        get_url = body.get("urls", {}).get("get")
        if not get_url:
            raise ThreeDEngineError("Replicate did not return a poll URL")
        for _ in range(60):  # up to ~60s
            time.sleep(1)
            req = urllib.request.Request(
                get_url,
                headers=self._headers,
                method="GET",
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                status = json.loads(resp.read().decode())
            if status.get("status") == "succeeded":
                output = status.get("output") or {}
                mesh_url = output.get("mesh_url") or output.get("video") or ""
                texture_url = output.get("texture_url")
                if not mesh_url:
                    raise ThreeDEngineError("Replicate output missing mesh_url")
                return mesh_url, texture_url
            if status.get("status") == "failed":
                raise ThreeDEngineError(f"Replicate prediction failed: {status.get('error')}")
        raise ThreeDEngineError("Replicate prediction timed out")


class HuggingFaceThreeDEngine(_RemoteThreeDEngine):
    """HuggingFace Inference API adapter."""

    def __init__(self) -> None:
        super().__init__(
            endpoint=f"https://api-inference.huggingface.co/models/{settings.HUGGINGFACE_MODEL_ID}",
            headers={"Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}"},
            model_ref=settings.HUGGINGFACE_MODEL_ID,
        )

    def synthesize(self, image_urls: list[str]) -> Tuple[str, Optional[str]]:
        body = self._post({"inputs": image_urls})
        mesh_url = body.get("mesh_url") or body.get("generated_mesh") or ""
        if not mesh_url:
            raise ThreeDEngineError(f"HF output missing mesh_url: {body!r}")
        return mesh_url, body.get("texture_url")


class ExternalWorkerThreeDEngine(_RemoteThreeDEngine):
    """Generic external GPU worker adapter."""

    def __init__(self) -> None:
        super().__init__(
            endpoint=settings.EXTERNAL_3D_WORKER_URL,
            headers={},
            model_ref="",
        )

    def synthesize(self, image_urls: list[str]) -> Tuple[str, Optional[str]]:
        body = self._post({"images": image_urls})
        mesh_url = body.get("mesh_url") or ""
        if not mesh_url:
            raise ThreeDEngineError(f"external worker missing mesh_url: {body!r}")
        return mesh_url, body.get("texture_url")


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------


def get_engine() -> ThreeDEngineAdapter:
    name = (settings.THREE_D_ENGINE or "fallback").lower()
    if name == "replicate":
        return ReplicateThreeDEngine()
    if name == "huggingface":
        return HuggingFaceThreeDEngine()
    if name == "external":
        return ExternalWorkerThreeDEngine()
    return FallbackThreeDEngine()


__all__ = [
    "ThreeDEngineAdapter",
    "ThreeDEngineError",
    "FallbackThreeDEngine",
    "get_engine",
]
