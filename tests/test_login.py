from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)
    login_page.login("test@example.com", "password123")



def test_invalid_login(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)

    login_page.login("test@example.com", "password123")

    expect(login_page.error_message).to_be_visible()

    
def test_valid_login(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    login_page = LoginPage(page)

    login_page.login("automationskeptic@gmail.com", "Admin@123")

    expect(login_page.valid_login_message).to_be_visible()

    message = login_page.valid_login_message.inner_text()
    print(f"Post-login message: {message}")
    
