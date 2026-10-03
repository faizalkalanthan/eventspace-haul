import pytest
from playwright.sync_api import Page


@pytest.fixture
def greenkart(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    return page