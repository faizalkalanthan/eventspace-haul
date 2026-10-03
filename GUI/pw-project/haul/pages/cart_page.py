from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_button = page.locator("img[alt='Cart']")
        self.proceed_to_checkout = page.get_by_text("PROCEED TO CHECKOUT")
        self.total_amount = page.locator(".totAmt")
        self.promo_code = page.get_by_placeholder("Enter promo code")
        self.apply_promo = page.get_by_text("Apply")


    def cart_product(self, product):
        product = self.page.locator("p.product-name").filter(has_text=product).first
        return product

    def enter_promo_code(self, code):
        self.promo_code.fill(code) 