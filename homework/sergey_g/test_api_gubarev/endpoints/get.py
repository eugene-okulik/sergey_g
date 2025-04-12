import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get all object')
    def get_all(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(self.url, headers=headers)
        self.json = self.response.json()
        assert self.response.status_code == 200, '200 is not 200'
        assert len(self.response.json()) >= 0, 'Not all objects returned'
        return self.response

    @allure.step('Get object by id')
    def get_by_id(self, object_id, headers=None):
        self.response = requests.put(f'{self.url}/{object_id}', headers=headers)
        self.json = self.response.json()
        return self.response
