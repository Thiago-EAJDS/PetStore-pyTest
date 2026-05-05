import pytest
from models.store_model import order_payload

class TestStore:

    def test_get_inventory(self, store_service):
        response = store_service.get_inventory()
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_place_order(self, store_service, created_pet):
        payload = order_payload(pet_id=created_pet["id"])
        response = store_service.place_order(payload)
        assert response.status_code == 200
        body = response.json()
        assert body["petId"] == created_pet["id"]
        assert body["status"] == "placed"

    def test_get_order_by_id(self, store_service, created_order):
        response = store_service.get_order(created_order["id"])
        assert response.status_code == 200
        assert response.json()["id"] == created_order["id"]

    def test_delete_order(self, store_service, created_pet):
        payload = order_payload(pet_id=created_pet["id"])
        order = store_service.place_order(payload).json()
        response = store_service.delete_order(order["id"])
        assert response.status_code == 200

    def test_get_deleted_order_returns_404(self, store_service, created_pet):
        payload = order_payload(pet_id=created_pet["id"])
        order = store_service.place_order(payload).json()
        store_service.delete_order(order["id"])
        response = store_service.get_order(order["id"])
        assert response.status_code == 404