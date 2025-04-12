import requests
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    def update_object(self, object_id, headers=None):
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{object_id}', json=body, headers=headers)
        assert (self.response.json()['data'])['price'] == 2049.99
