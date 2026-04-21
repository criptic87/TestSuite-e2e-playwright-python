from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"
        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-link"]')
        self.image_src = page.locator('')
        self.menu_button = page.locator('#react-burger-menu-btn')
        self.logout_button = page.locator('[data-test="logout-sidebar-link"]')
    
    def should_be_loaded(self):
        expect(self.page).to_have_url(self.url)
        expect(self.shopping_cart).to_be_visible(timeout=10000)
    
    def navigate(self):
        self.page.goto(self.url)

    def logout(self):
        expect(self.menu_button).to_be_visible()
        self.menu_button.click()

        expect(self.logout_button).to_be_visible()
        self.logout_button.click()
    
        expect(self.page).to_have_url("https://www.saucedemo.com/")
    

"""
    def add_to_cart(self):
        self.add_to_cart_button.click()
"""