from conftest import authenticated_page


def test_event_page(authenticated_page):
    authenticated_page.goto(
        "https://eventhub.rahulshettyacademy.com/events/284"
    )


