import requests


def all_objects():
    response = requests.get('https://api.restful-api.dev/objects').json()
    print(response)
    assert len(response) == 13, 'Not all objects returned'


def add_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post('https://api.restful-api.dev/objects', json=body,
                             headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    return response.json()['id']


def update_object():
    object_id = add_object()
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
    headers = {"content-type": "application/json"}
    response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=body,
                            headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert (response.json()['data'])['price'] == 2049.99


def patch_object():
    object_id = add_object()
    body = {
        "name": "Apple MacBook Pro 16 (UPD)"
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(f'https://api.restful-api.dev/objects/{object_id}', json=body,
                              headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Apple MacBook Pro 16 (UPD)'


def delete_object():
    object_id = add_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['message'] == f'Object with id = {object_id} has been deleted.'


add_object()
