"""Edge case tests for the otomotif backend API"""
import importlib

# Use importlib to handle modules starting with digits
_3d_mod = importlib.import_module("app.routes.3d")
diagnosis_mod = importlib.import_module("app.routes.diagnosis")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class Test3dEdgeCases:
    """Test edge cases for /api/v1/3d/modify endpoint"""

    def test_upload_file_too_large(self):
        """Upload file > 5MB should return 422 (backend validation)"""
        large_content = b"x" * (5 * 1024 * 1024 + 1)  # 5MB + 1 byte
        files = {"file": ("large.bin", large_content, "application/octet-stream")}
        data = {"part_id": "body"}
        response = client.post("/api/v1/3d/modify", files=files, data=data)
        assert response.status_code == 422

    def test_upload_non_image_file(self):
        """Upload non-image file (.txt, .exe) should return 422"""
        txt_content = b"this is a test text file"
        files = {"file": ("test.txt", txt_content, "text/plain")}
        data = {"part_id": "body"}
        response = client.post("/api/v1/3d/modify", files=files, data=data)
        assert response.status_code == 422

    def test_empty_part_id(self):
        """Empty part_id should be rejected with 422"""
        content = b"test content"
        files = {"file": ("test.jpg", content, "image/jpeg")}
        data = {"part_id": ""}
        response = client.post("/api/v1/3d/modify", files=files, data=data)
        assert response.status_code == 422

    def test_part_id_with_special_chars(self):
        """part_id with special characters should be rejected"""
        content = b"test content"
        files = {"file": ("test.jpg", content, "image/jpeg")}
        data = {"part_id": "body<script>"}
        response = client.post("/api/v1/3d/modify", files=files, data=data)
        # Backend validates part_id alphanumeric/UUID - expect 422
        assert response.status_code == 422


class TestDiagnosisEdgeCases:
    """Test edge cases for /api/v1/diagnosis/analyze endpoint"""

    def test_empty_user_story(self):
        """Empty user_story should return 422"""
        response = client.post(
            "/api/v1/diagnosis/analyze",
            json={"symptom_text": ""},
        )
        assert response.status_code == 422

    def test_whitespace_only_user_story(self):
        """Whitespace-only user_story should return 422"""
        response = client.post(
            "/api/v1/diagnosis/analyze",
            json={"symptom_text": "   "},
        )
        assert response.status_code == 422

    def test_valid_user_story(self):
        """Valid user_story should accept"""
        response = client.post(
            "/api/v1/diagnosis/analyze",
            json={"symptom_text": "Engine makes knocking sound when accelerating"},
        )
        assert response.status_code == 200


class TestAuthEdgeCases:
    """Test edge cases for auth endpoints"""

    def test_empty_payload(self):
        """Empty payload should be handled gracefully"""
        response = client.post("/api/v1/auth/register", json={})
        # Should not crash - expect 422 or 400
        assert response.status_code in (400, 422)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
