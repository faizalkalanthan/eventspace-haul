from playwright.sync_api import Page, expect

class EventPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("input[placeholder*='Search']")
        self.full_name = page.get_by_label("Full Name")
        self.email = page.get_by_label("Email")
        self.phone_number = page.get_by_label("Phone Number")
        self.confirm_booking_button = page.get_by_role("button", name="Confirm Booking")

    def search_event(self, keyword: str):
        self.search_input.fill(keyword)

    def book_ticket(self, name: str, email: str, phone: str):
        self.full_name.fill(name)
        self.email.fill(email)
        self.phone_number.fill(phone)
        self.confirm_booking_button.click()