from utils.helpers import random_id, random_username, random_email

def user_payload(username=None):
    uname = username or random_username()
    return {
        "id": random_id(),
        "username": uname,
        "firstName": "Test",
        "lastName": "User",
        "email": random_email(),
        "password": "Test@1234",
        "phone": "11999999999",
        "userStatus": 1
    }