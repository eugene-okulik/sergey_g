from locust import task, HttpUser


class ObjectUser(HttpUser):
    object_id = None

    def on_start(self):
        body = {
            "name": "Test Object",
            "data": {
                "year": 2023,
                "price": 999.99,
                "CPU model": "Test CPU",
                "Hard disk size": "Test Size"
            }
        }
        response = self.client.post('/objects', json=body, headers={'Content-type': 'application/json'})
        assert 'id' in response.json(), 'Check for the id in the response'
        self.object_id = response.json()['id']

    @task(2)
    def get_all_object(self):
        self.client.get('/objects', headers={'Content-type': 'application/json'})

    @task(3)
    def patch_object(self, object_id):
        body = {
            "name": "Apple MacBook Pro 16 (UPD)"
        }
        self.client.patch(f'/objects/{object_id}', json=body, headers={'Content-type': 'application/json'})

    @task(4)
    def update_object(self, object_id):
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
        self.client.put(f'/objects/{object_id}', json=body, headers={'Content-type': 'application/json'})

    @task(1)
    def delete_object(self, object_id):
        self.client.delete(f'/objects/{object_id}', headers={'Content-type': 'application/json'})
