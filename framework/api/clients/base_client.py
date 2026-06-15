import requests
from framework.config.config import BASE_URL
import logging

logger = logging.getLogger(__name__)

class BaseClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        logger.info(f"GET request to {self.base_url}{endpoint}")
        response = requests.get(f"{self.base_url}{endpoint}")
        logger.info(f"Response status: {response.status_code}")
        return response

    def post(self, endpoint, data=None, headers=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def put(self, endpoint, data=None, headers=None):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )