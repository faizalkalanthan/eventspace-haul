
def test_event_page(authenticated_page):
    authenticated_page.goto("https://eventhub.rahulshettyacademy.com/events/284")

def test_eventhub(page: Page):
    page.goto("https://eventhub.rahulshettyacademy.com/events/284")

