from playwright.sync_api import expect
from pages.event_page import EventPage

BASE_URL = "https://eventhub.rahulshettyacademy.com"


def test_browse_events_page(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events")
    expect(authenticated_page).to_have_url(f"{BASE_URL}/events")
    expect(authenticated_page.locator("#nav-events")).to_be_visible()
    expect(authenticated_page.locator('a[href^="/events/"]').first).to_be_visible()


def test_my_bookings_page(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/bookings")
    expect(authenticated_page).to_have_url(f"{BASE_URL}/bookings")
    expect(authenticated_page.locator("#nav-bookings")).to_be_visible()


def test_event_details_and_booking_form(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events/284")
    expect(authenticated_page.get_by_role("heading", name="Hollywood Monsoon Night — Los Angeles")).to_be_visible()
    expect(authenticated_page.get_by_text("Book Tickets")).to_be_visible()
    expect(authenticated_page.get_by_role("button", name="Confirm Booking")).to_be_visible()


def test_search_events(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events")
    event_page = EventPage(authenticated_page)
    event_page.search_event("Hollywood")
    expect(authenticated_page.get_by_text("Hollywood Monsoon Night")).to_be_visible()


def test_complete_booking_and_verify_in_my_bookings(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events/284")
    event_page = EventPage(authenticated_page)
    event_page.book_ticket("Automation SDET", "sdet.test@example.com", "9876543210")
    authenticated_page.goto(f"{BASE_URL}/bookings")
    expect(authenticated_page.get_by_text("Hollywood Monsoon Night").first).to_be_visible()


def test_required_field_validation(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events/284")
    event_page = EventPage(authenticated_page)
    # Attempting to click confirm without filling details
    event_page.confirm_booking_button.click()
    expect(event_page.confirm_booking_button).to_be_visible()