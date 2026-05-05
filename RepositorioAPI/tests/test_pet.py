from models.pet_model import pet_payload

class TestPet:

    def test_create_pet_success(self, pet_service):
        payload = pet_payload()
        response = pet_service.create_pet(payload)
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == payload["id"]
        assert body["name"] == payload["name"]
        assert body["status"] == "available"

    def test_get_pet_by_id(self, pet_service, created_pet):
        response = pet_service.get_pet(created_pet["id"])
        assert response.status_code == 200
        assert response.json()["id"] == created_pet["id"]

    def test_update_pet(self, pet_service, created_pet):
        updated = {**created_pet, "name": "updated_dog", "status": "sold"}
        response = pet_service.update_pet(updated)
        assert response.status_code == 200
        body = response.json()
        assert body["name"] == "updated_dog"
        assert body["status"] == "sold"

    def test_find_pets_by_status_available(self, pet_service):
        response = pet_service.find_by_status("available")
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        assert all(p["status"] == "available" for p in pets)

    def test_find_pets_by_status_sold(self, pet_service):
        response = pet_service.find_by_status("sold")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_delete_pet(self, pet_service):
        payload = pet_payload()
        pet_service.create_pet(payload)
        response = pet_service.delete_pet(payload["id"])
        assert response.status_code == 200

    def test_get_deleted_pet_returns_404(self, pet_service):
        payload = pet_payload()
        pet_service.create_pet(payload)
        pet_service.delete_pet(payload["id"])
        response = pet_service.get_pet(payload["id"])
        assert response.status_code == 404
