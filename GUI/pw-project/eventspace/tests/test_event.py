from playwright.sync_api import expect

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
    expect(authenticated_page.get_by_text("Full Name*")).to_be_visible()
    expect(authenticated_page.get_by_text("Phone Number*")).to_be_visible()


def test_search_events(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events")
    # Use a flexible partial attribute selector for the search input
    authenticated_page.locator("input[placeholder*='Search']").fill("Hollywood")
    expect(authenticated_page.get_by_text("Hollywood Monsoon Night")).to_be_visible()


def test_complete_booking_and_verify_in_my_bookings(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/events/284")
    authenticated_page.get_by_label("Full Name").fill("Automation SDET")
    authenticated_page.get_by_label("Email").fill("sdet.test@example.com")
    authenticated_page.get_by_label("Phone Number").fill("9876543210")
    authenticated_page.get_by_role("button", name="Confirm Booking").click()
    authenticated_page.goto(f"{BASE_URL}/bookings")
    expect(authenticated_page.get_by_text("Hollywood Monsoon Night").first).to_be_visible() 