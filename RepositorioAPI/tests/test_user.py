import pytest
from models.user_model import user_payload

class TestUser:

    def test_create_user(self, user_service):
        payload = user_payload()
        response = user_service.create_user(payload)
        assert response.status_code == 200

    def test_get_user(self, user_service, created_user):
        response = user_service.get_user(created_user["username"])
        assert response.status_code == 200
        assert response.json()["username"] == created_user["username"]

    def test_login(self, user_service, created_user):
        response = user_service.login(created_user["username"], created_user["password"])
        assert response.status_code == 200
        assert "logged in" in response.json().get("message", "").lower()

    def test_update_user(self, user_service, created_user):
        updated = {**created_user, "firstName": "Updated"}
        response = user_service.update_user(created_user["username"], updated)
        assert response.status_code == 200

    def test_logout(self, user_service):
        response = user_service.logout()
        assert response.status_code == 200

    def test_delete_user(self, user_service):
        payload = user_payload()
        user_service.create_user(payload)
        response = user_service.delete_user(payload["username"])
        assert response.status_code == 200

    def test_get_deleted_user_returns_404(self, user_service):
        payload = user_payload()
        user_service.create_user(payload)
        user_service.delete_user(payload["username"])
        response = user_service.get_user(payload["username"])
        assert response.status_code == 404
