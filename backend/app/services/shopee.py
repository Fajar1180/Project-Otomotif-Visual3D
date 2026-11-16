"""Shopee Affiliate service: product search + affiliate links.

Ponytail: real Shopee Affiliate API requires app_id/app_secret credentials
and network access. This stub wraps HTTP calls with Redis cache + in-memory
fallback, static fallback parts list, click tracking, and naive rate-limit
handling. Swap _call_shopee_api for the genuine SDK when credentials exist.
Upgrade path: wire settings.shopee_app_id / settings.shopee_app_secret.
"""
from __future__ import annotations

import time
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode, urlparse, parse_qsl, urlunparse

import httpx


from config import (
    JWT_SECRET,
    JWT_EXPIRE_MINUTES,
    DATABASE_URL,
    REDIS_URL,
    SHOPEE_APP_ID,
    SHOPEE_APP_KEY,
    SHOPEE_APP_SECRET,
)

# Ponytail: Redis cache is preferred; fall back to in-memory dict so tests
# run without a Redis instance.
try:  # pragma: no cover - redis optional
    import redis as _redis

    _cache = _redis.from_url(settings.redis_url, decode_responses=True)
except Exception:  # pragma: no cover
    _cache = None

_IN_MEMORY_CACHE: dict[str, tuple[float, Any]] = {}
_CLICK_COUNTS: dict[str, int] = {}

STATIC_PARTS: List[Dict[str, Any]] = [
    {
        "item_id": "static-1",
        "name": "Kampas Rem Depan Avanza",
        "brand": "Toyota",
        "price": 180000,
        "currency": "IDR",
        "shopee_url": "https://shp.ee/static1",
    },
    {
        "item_id": "static-2",
        "name": "Oli Mesin 10W-40 1L",
        "brand": "Generic",
        "price": 75000,
        "currency": "IDR",
        "shopee_url": "https://shp.ee/static2",
    },
    {
        "item_id": "static-3",
        "name": "Aki 35A",
        "brand": "Generic",
        "price": 450000,
        "currency": "IDR",
        "shopee_url": "https://shp.ee/static3",
    },
]


def _cache_get(key: str) -> Optional[Any]:
    if _cache is not None:
        try:
            import json

            raw = _cache.get(key)
            if raw:
                return json.loads(raw)
        except Exception:
            pass
    entry = _IN_MEMORY_CACHE.get(key)
    if entry and entry[0] > time.time():
        return entry[1]
    return None


def _cache_set(key: str, value: Any, ttl: int = 3600) -> None:
    if _cache is not None:
        try:
            import json

            _cache.setex(key, ttl, json.dumps(value))
            return
        except Exception:
            pass
    _IN_MEMORY_CACHE[key] = (time.time() + ttl, value)


def track_click(item_id: str) -> int:
    """Increment click counter for an affiliate link; return new count."""
    _CLICK_COUNTS[item_id] = _CLICK_COUNTS.get(item_id, 0) + 1
    return _CLICK_COUNTS[item_id]


def _call_shopee_api(query: str, limit: int) -> Optional[List[Dict[str, Any]]]:
    """Call Shopee Affiliate Search API. Returns None when unavailable."""
    try:
        resp = httpx.get(
            "https://openapi.shopee.com/affiliate/search",
            params={"keyword": query, "limit": limit},
            timeout=5.0,
        )
        if resp.status_code == 429:
            return None  # rate limited -> caller falls back
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", {}).get("items", [])
    except Exception:
        return None


def search_products(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Search Shopee products with cache + static fallback."""
    cache_key = f"shopee:search:{query.lower()}:{limit}"
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached

    items = _call_shopee_api(query, limit)
    if items is None:  # network down or rate limited
        items = STATIC_PARTS[:limit]

    _cache_set(cache_key, items)
    return items


def generate_affiliate_link(item_id: str, source: str = "web", campaign: str = "affiliate") -> str:
    """Build an affiliate link for an item with UTM tracking params.

    Falls back to the static parts list when the item is not a live Shopee
    result. UTM params: utm_source, utm_medium=affiliate, utm_campaign.
    """
    target = None
    for part in STATIC_PARTS:
        if part["item_id"] == item_id:
            target = part["shopee_url"]
            break
    if target is None:
        raise ValueError(f"Tidak dapat menemukan link afiliasi untuk item_id={item_id}")

    parsed = urlparse(target)
    query = dict(parse_qsl(parsed.query))
    query.update(
        {
            "utm_source": source,
            "utm_medium": "affiliate",
            "utm_campaign": campaign,
        }
    )
    return urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, urlencode(query), parsed.fragment)
    )
