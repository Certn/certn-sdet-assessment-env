from playwright.sync_api import (
    Browser,
    Page,
    PlaywrightContextManager,
    sync_playwright
)
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def client_email() -> str:
    return "terry.chiu+client@certn.co"


@pytest.fixture
def client_password() -> str:
    return "Certn@123"


@pytest.fixture
def client_portal_login_url() -> str:
    return "https://client.development.certn.co/"


#############################
# Selenium fixtures         #
#############################

@pytest.fixture(scope="session")
def installed_driver_path() -> str:
    return ChromeDriverManager().install()


@pytest.fixture
def selenium_webdriver_with_chrome(
    installed_driver_path: str,
    client_portal_login_url: str
) -> webdriver.Remote:
    local_service = webdriver.chrome.service.Service(installed_driver_path)
    driver = webdriver.Chrome(service=local_service)
    driver.get(client_portal_login_url)
    yield driver
    driver.quit()

#############################
# End of Selenium fixtures  #
#############################


#################################
# Playwright fixtures           #
#################################

@pytest.fixture
def playwright():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


@pytest.fixture
def playwright_chrome_browser(
    playwright: PlaywrightContextManager,
    client_portal_login_url: str
) -> Page:
    browser: Browser = playwright.chromium.launch(headless=False)
    playwright_page = browser.new_page()
    playwright_page.goto(client_portal_login_url)
    return playwright_page

#################################
# End of Playwright fixtures    #
#################################
