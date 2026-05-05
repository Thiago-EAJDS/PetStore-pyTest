import requests
import logging

logger = logging.getLogger(__name__)

class BaseService:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, params=params)
        logger.info(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def post(self, endpoint, payload):
        url = f"{self.BASE_URL}{endpoint}"
        logger.info(f"POST {url} | Body: {payload}")
        response = self.session.post(url, json=payload)
        logger.info(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def put(self, endpoint, payload):
        url = f"{self.BASE_URL}{endpoint}"
        logger.info(f"PUT {url} | Body: {payload}")
        response = self.session.put(url, json=payload)
        logger.info(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url)
        logger.info(f"Response [{response.status_code}]: {response.text[:200]}")
        return response
