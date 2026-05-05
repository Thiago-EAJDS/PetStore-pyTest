import random
import string
from faker import Faker

fake = Faker()

def random_id():
    return random.randint(10000, 99999)

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_username():
    return fake.user_name() + str(random.randint(100, 999))

def random_email():
    return fake.email()