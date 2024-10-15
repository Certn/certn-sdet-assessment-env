import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def client_email() -> str:
    return "terry.chiu+client@certn.co"


@pytest.fixture
def client_password() -> str:
    return "Certn@123"


@pytest.fixture(scope="session")
def installed_driver_path() -> str:
    return ChromeDriverManager().install()


@pytest.fixture
def client_portal_login_url() -> str:
    return "https://client.development.certn.co/"


@pytest.fixture
def selenium_webdriver_with_chrome(installed_driver_path: str, client_portal_login_url) -> webdriver.Remote:
    local_service = webdriver.chrome.service.Service(installed_driver_path)
    driver = webdriver.Chrome(service=local_service)
    driver.get(client_portal_login_url)
    yield driver
    driver.quit()
