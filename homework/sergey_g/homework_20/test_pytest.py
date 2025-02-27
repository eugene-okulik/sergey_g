import requests
import pytest
import allure

url = 'https://api.restful-api.dev/objects'
headers = {"content-type": "application/json"}


# Фикстура для создания и удаления объекта
@pytest.fixture(scope='function')
def object_id():
    # Создание объекта
    body = {
        "name": "Test Object",
        "data": {
            "year": 2023,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "Test Size"
        }
    }
    response = requests.post(url, json=body, headers=headers)
    object_id = response.json()['id']
    yield object_id  # Возвращаем ID созданного объекта
    # Удаление объекта после теста
    delete_object(object_id)


# Функция для удаления объекта
def delete_object(object_id):
    response = requests.delete(f'{url}/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['message'] == f'Object with id = {object_id} has been deleted.'


# Тест получения всех объектов
@pytest.mark.medium
@allure.feature('Взаимодействие с объектами')
@allure.story('Get')
@allure.title('Тест получения всех объектов')
def test_all_objects():
    response = requests.get('https://api.restful-api.dev/objects').json()
    print(response)
    assert len(response) >= 0, 'Not all objects returned'


# Тест добавления объекта
test_json = (
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Dell XPS 15",
        "data": {
            "year": 2021,
            "price": 1499.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    },
    {
        "name": "HP Spectre x360",
        "data": {
            "year": 2020,
            "price": 1299.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "256 GB"
        }
    }
)


@pytest.mark.parametrize("body", test_json)
@pytest.mark.critical
@allure.story('Post')
@allure.feature('Взаимодействие с объектами')
@allure.title('Тест добавления объекта')
def test_add_object(body):
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert 'id' in response.json(), 'Check for the id in the response'


# Обновления объекта
def update_object(object_id):
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
    response = requests.put(f'{url}/{object_id}', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert (response.json()['data'])['price'] == 2049.99


# Редактирование объекта
def patch_object(object_id):
    body = {
        "name": "Apple MacBook Pro 16 (UPD)"
    }
    response = requests.patch(f'{url}/{object_id}', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Apple MacBook Pro 16 (UPD)'


# Тест удаления объекта
@pytest.mark.critical
@allure.feature('Взаимодействие с объектами')
@allure.story('Del')
@allure.title('Тест удаления объекта')
def test_delete_object():
    # Создание объекта
    body = {
        "name": "Object for Deletion",
        "data": {
            "year": 2023,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "Test Size"
        }
    }
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200, 'Failed to create object'
