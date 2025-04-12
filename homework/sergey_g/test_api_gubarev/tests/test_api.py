import pytest
import allure


@pytest.mark.medium
@allure.feature('Взаимодействие с объектами')
@allure.story('Get')
@allure.title('Тест получения всех объектов')
def test_all_objects(get_endpoint, checks):
    get_endpoint.get_all()
    checks.response = get_endpoint.response
    checks.check_that_response_is_200()


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
def test_add_object(create_endpoint, body, checks):
    create_endpoint.create_new_object(body)
    checks.response = create_endpoint.response
    checks.check_that_response_is_200()


@pytest.mark.critical
@allure.story('Put')
@allure.feature('Взаимодействие с объектами')
@allure.title('Тест обновления объекта')
def test_put_object(update_endpoint, object_id, checks):
    update_endpoint.update_object(object_id)
    checks.response = update_endpoint.response
    checks.check_that_response_is_200()


@pytest.mark.critical
@allure.story('Patch')
@allure.feature('Взаимодействие с объектами')
@allure.title('Тест обновления объекта')
def test_patch_object(patch_endpoint, object_id, checks):
    patch_endpoint.patch_object(object_id)
    checks.response = patch_endpoint.response
    checks.check_that_response_is_200()


@pytest.mark.critical
@allure.feature('Взаимодействие с объектами')
@allure.story('Del')
@allure.title('Тест удаления объекта')
def test_delete_object(delete_endpoint, checks):
    body = {
        "name": "Object for Deletion",
        "data": {
            "year": 2023,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "Test Size"
        }
    }
    delete_endpoint.delete_object(body)
    checks.response = delete_endpoint.response
    checks.check_bad_requiest_is_404()
