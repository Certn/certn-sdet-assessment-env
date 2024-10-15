import time

from playwright.sync_api import Page


def enter_username(page: Page, username: str):
    page.locator("input#username").click()
    page.locator("input#username").fill(username)
    page.locator("button[type=submit]").click()


def enter_password():
    raise NotImplementedError


def test_with_playwright__sign_in_to_client_portal(
    playwright_chrome_browser: Page,
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
    # - `playwright_chrome_browser` is a working Playwright page in Chrome    #
    # - `client_email` is an email address you can safely use for the test    #
    # - `client_password` is a password                                       #
    # - the above are provided by pytest fixtures in the conftest.py file     #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    enter_username(playwright_chrome_browser, client_email)
    enter_password()

    time.sleep(10)
