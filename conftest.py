import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
load_dotenv()

@pytest.fixture
def login_page(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    return LoginPage(page)