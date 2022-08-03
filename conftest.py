import faker
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def fake() -> faker.Faker:
    return faker.Faker()


@pytest.fixture
def user_email(fake: faker.Faker) -> str:
    return fake.unique.email()


@pytest.fixture(scope="session")
def installed_driver_path() -> str:
    return ChromeDriverManager().install()


@pytest.fixture
def driver(installed_driver_path: str) -> webdriver.Remote:
    local_service = webdriver.chrome.service.Service(installed_driver_path)
    driver = webdriver.Chrome(service=local_service)
    driver.get("https://quora.com")

    yield driver

    driver.quit()
