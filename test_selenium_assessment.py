import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def enter_username(webdriver: webdriver.Remote, username: str):
    webdriver.find_element(By.CSS_SELECTOR, "input#username").click()
    webdriver.find_element(By.CSS_SELECTOR, "input#username").send_keys(
        username
    )
    webdriver.find_elements(By.CSS_SELECTOR, "button[type=submit]")[0].click()


def enter_password():
    raise NotImplementedError


def test_with_selenium__sign_in_to_client_portal(
    selenium_webdriver_with_chrome: webdriver.Remote,
    client_email: str,
    client_password: str,
) -> None:
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #     Fill in the blanks exercise!                                        #
    #                                                                         #
    #   Here's the login page for a Certn customer. The challenge here is to  #
    #   complete the signin workflow by filling out the "enter_password"      #
    #   function, as well as what you would validate on to ensure a           #
    #   successful signin.                                                    #
    #                                                                         #
    # Good to know:                                                           #
    # - `selenium_webdriver_with_chrome` is a working Selenium WebDriver      #
    # - `client_email` is an email address you can safely use for the test    #
    # - `client_password` is a password                                       #
    # - the above are provided by pytest fixtures in the conftest.py file     #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    enter_username(selenium_webdriver_with_chrome, client_email)
    enter_password()

    time.sleep(10)
