from playwright.sync_api import Page
from playwright.sync_api import expect

from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_checkout(page: Page):

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    products_page.search_product("Brocolli")
    products_page.add_product_to_cart()

    cart_page.cart_button.click()
    cart_page.proceed_to_checkout.click()

    print(page.locator(".totAmt").inner_text())
    expect(cart_page.total_amount).to_have_text("120")

    cart_page.enter_promo_code("rahulshettyacademy")
    cart_page.apply_promo.click()

    expect(cart_page.promo_info).to_have_text("Code applied ..!")
