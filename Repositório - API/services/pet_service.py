from services.base_service import BaseService

class PetService(BaseService):
    def create_pet(self, payload):
        return self.post("/pet", payload)

    def get_pet(self, pet_id):
        return self.get(f"/pet/{pet_id}")

    def update_pet(self, payload):
        return self.put("/pet", payload)

    def delete_pet(self, pet_id):
        return self.delete(f"/pet/{pet_id}")

    def find_by_status(self, status):
        return self.get("/pet/findByStatus", params={"status": status})