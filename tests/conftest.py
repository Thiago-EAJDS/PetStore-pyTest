import pytest
from services.pet_service import PetService
from services.store_service import StoreService
from services.user_service import UserService
from models.pet_model import pet_payload
from models.store_model import order_payload
from models.user_model import user_payload

@pytest.fixture(scope="session")
def pet_service():
    return PetService()

@pytest.fixture(scope="session")
def store_service():
    return StoreService()

@pytest.fixture(scope="session")
def user_service():
    return UserService()

@pytest.fixture(scope="module")
def created_pet(pet_service):
    payload = pet_payload()
    response = pet_service.create_pet(payload)
    assert response.status_code == 200
    return response.json()

@pytest.fixture(scope="module")
def created_order(store_service, created_pet):
    payload = order_payload(pet_id=created_pet["id"])
    response = store_service.place_order(payload)
    assert response.status_code == 200
    return response.json()

@pytest.fixture(scope="module")
def created_user(user_service):
    payload = user_payload()
    response = user_service.create_user(payload)
    assert response.status_code == 200
    return payload  # retorna o payload pois a API não devolve o objeto criado