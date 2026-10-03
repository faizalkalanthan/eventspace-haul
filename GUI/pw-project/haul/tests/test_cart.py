from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_add_product_to_cart(page):

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    products_page = ProductsPage(page)

    products_page.search_product("Brocolli")
    products_page.add_product_to_cart()

    expect(products_page.quantity).to_have_value("1")
    

def test_validate_product_in_cart(page):

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    products_page.search_product("Brocolli")
    products_page.add_product_to_cart()

    cart_page.cart_button.click()
    page.wait_for_selector("p.product-name")
    expect(cart_page.cart_product("Brocolli")).to_be_visible()



    
