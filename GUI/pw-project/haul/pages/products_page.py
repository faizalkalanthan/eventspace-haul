from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.search_box = page.get_by_placeholder("Search for Vegetables and Fruits")
        self.add_to_cart_button = page.get_by_role("button", name="ADD TO CART").first
        self.quantity = page.locator("input.quantity")
      

    def search_product(self, product_name):
        self.search_box.fill(product_name)
 
    def add_product_to_cart(self):
        self.add_to_cart_button.click()
        self.page.wait_for_timeout(3000)


    