from conftest import authenticated_page
from pages.login_page import LoginPage
from playwright.sync_api import Page
from playwright.sync_api import expect
import os

def test_login(page: Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)
    login_page.login("test@example.com", "password123")



def test_invalid_login(page: Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)

    login_page.login("test@example.com", "password123")

    expect(login_page.error_message).to_be_visible()


    
def test_valid_login(page: Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)

    login_page.login("automationskeptic@gmail.com", "Admin@123")

    expect(login_page.valid_login_message).to_be_visible()

    message = login_page.valid_login_message.inner_text()
    print(f"Post-login message: {message}")



def test_valid_login_using_fixture(login_page):
    login_page.login("automationskeptic@gmail.com", "Admin@123")

    expect(login_page.valid_login_message).to_be_visible()    



def test_invalid_login_using_fixture(login_page):
    login_page.login("test@example.com", "password123")

    expect(login_page.error_message).to_be_visible()



def test_valid_login_using_env_variables(login_page):
    email = os.getenv("EVENTHUB_EMAIL")
    password = os.getenv("EVENTHUB_PASSWORD")

    login_page.login(email, password)

    expect(login_page.valid_login_message).to_be_visible()



def test_save_auth_state(authenticated_page):
    expect(
        authenticated_page.get_by_role("button", name="Logout")
    ).to_be_visible()



