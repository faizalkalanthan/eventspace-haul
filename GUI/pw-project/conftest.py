import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
load_dotenv()

@pytest.fixture
def login_page(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    return LoginPage(page)


@pytest.fixture
def save_auth_state(page):
    email = os.getenv("EVENTHUB_EMAIL")
    password = os.getenv("EVENTHUB_PASSWORD")

    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)
    login_page.login(email, password)

    page.get_by_role("button", name="Logout").wait_for()

    page.context.storage_state(
        path="playwright/.auth/user.json"
    )

    return page


@pytest.fixture
def authenticated_page(browser):
    context = browser.new_context(
        storage_state="playwright/.auth/user.json"
    )

    page = context.new_page()

    yield page

    context.close()