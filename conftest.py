import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    return LoginPage(page)