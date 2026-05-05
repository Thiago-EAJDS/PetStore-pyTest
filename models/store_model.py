from utils.helpers import random_id

def order_payload(pet_id=None, order_id=None):
    return {
        "id": order_id or random_id(),
        "petId": pet_id or random_id(),
        "quantity": 1,
        "shipDate": "2025-01-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }