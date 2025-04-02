import requests
from endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    def patch_object(self, object_id, headers=None):
        body = {
            "name": "Apple MacBook Pro 16 (UPD)"
        }
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{object_id}', json=body, headers=headers)
        assert self.response.json()['name'] == 'Apple MacBook Pro 16 (UPD)'
