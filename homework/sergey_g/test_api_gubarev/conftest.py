import pytest
from endpoints.get import GetObject
from endpoints.post import CreateObject
from endpoints.put import UpdateObject
from endpoints.patch import PatchObject
from endpoints.delete import DeleteObject
from utils.checks import Checks


@pytest.fixture()
def get_endpoint():
    return GetObject()


@pytest.fixture()
def create_endpoint():
    return CreateObject()


@pytest.fixture()
def update_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def checks():
    return Checks()


@pytest.fixture(scope='function')
def object_id(create_endpoint, delete_endpoint):
    body = {
        "name": "Test Object",
        "data": {
            "year": 2023,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "Test Size"
        }
    }
    create_endpoint.create_new_object(body)
    yield create_endpoint.object_id
    delete_endpoint.delete_object(create_endpoint.object_id)


@pytest.fixture(scope='session', autouse=True)
def settings_tests():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def around_tests():
    print("\nbefore test")
    yield
    print("\nafter test")
