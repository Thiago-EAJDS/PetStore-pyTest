from utils.helpers import random_id, random_string

def pet_payload(pet_id=None):
    return {
        "id": pet_id or random_id(),
        "category": {"id": 1, "name": "Dogs"},
        "name": f"dog_{random_string()}",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
    }