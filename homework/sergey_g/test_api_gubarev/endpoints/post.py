import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Create new post')
    def create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.response_json = self.response.json()

    @allure.step('Create object')
    def create_object(self, headers=None):
        body = {
            "name": "Test Object",
            "data": {
                "year": 2023,
                "price": 999.99,
                "CPU model": "Test CPU",
                "Hard disk size": "Test Size"
            }
        }
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        self.object_id = self.response.json()['id']
        return self.object_id
