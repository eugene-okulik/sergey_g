import requests
import allure
from endpoints.endpoint import Endpoint


class GetPost(Endpoint):

    @allure.step('Get all post')
    def get_all(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(self.url, headers=headers)
        self.json = self.response.json()
        print(self.response.json())
        return self.response

    @allure.step('Get post by id')
    def get_by_id(self, post_id, headers=None):
        self.response = requests.put(f'{self.url}/{post_id}', headers=headers)
        self.json = self.response.json()
        return self.response
