import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        assert 'id' in self.response.json(), 'Check for the id in the response'
        self.object_id = self.response.json()['id']
        return self.object_id
