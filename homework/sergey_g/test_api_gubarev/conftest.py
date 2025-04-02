import pytest
from endpoints.get import GetPost
from endpoints.post import CreatePost
from endpoints.put import UpdatePost
from endpoints.patch import PatchPost
from endpoints.delete import DeletePost
from utils.checks import Checks


@pytest.fixture()
def get_endpoint():
    return GetPost()


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def checks():
    return Checks()


# Фикстура для создания и удаления объекта
@pytest.fixture(scope='function')
def object_id(create_post_endpoint, delete_post_endpoint):
    create_post_endpoint.create_object()
    yield create_post_endpoint.object_id
    delete_post_endpoint.delete_object(create_post_endpoint.object_id)


# Фикстура для общего начала и завершения тестирования
@pytest.fixture(scope='session', autouse=True)
def settings_tests():
    print("\nStart testing")
    yield
    print("\nTesting completed")


# Фикстура для действий перед и после каждого теста
@pytest.fixture(autouse=True)
def around_tests():
    print("\nbefore test")
    yield
    print("\nafter test")
