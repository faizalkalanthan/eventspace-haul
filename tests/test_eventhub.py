from playwright.sync_api import Page


def test_eventhub(page: Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    print("TITLE:", page.title())
    print("URL:", page.url)

    page.wait_for_timeout(5000)