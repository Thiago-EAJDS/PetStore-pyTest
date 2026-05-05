from services.base_service import BaseService

class StoreService(BaseService):
    def place_order(self, payload):
        return self.post("/store/order", payload)

    def get_order(self, order_id):
        return self.get(f"/store/order/{order_id}")

    def delete_order(self, order_id):
        return self.delete(f"/store/order/{order_id}")

    def get_inventory(self):
        return self.get("/store/inventory")
