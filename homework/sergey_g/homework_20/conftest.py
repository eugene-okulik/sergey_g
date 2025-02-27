import pytest


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
