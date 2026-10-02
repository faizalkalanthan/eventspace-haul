from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.error_message = page.get_by_text("Invalid email or password")

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.sign_in_button.click()
        