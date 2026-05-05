from services.base_service import BaseService

class UserService(BaseService):
    def create_user(self, payload):
        return self.post("/user", payload)

    def get_user(self, username):
        return self.get(f"/user/{username}")

    def update_user(self, username, payload):
        return self.put(f"/user/{username}", payload)

    def delete_user(self, username):
        return self.delete(f"/user/{username}")

    def login(self, username, password):
        return self.get("/user/login", params={"username": username, "password": password})

    def logout(self):
        return self.get("/user/logout")
