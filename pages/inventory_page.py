from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"
        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
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
    
    def add_to_cart(self, product_name):
        selector = f'[data-test="add-to-cart-{product_name}"]'
        self.page.locator(selector).click()
    
    def remove_from_cart(self, product_name):
        selector = f'[data-test="remove-{product_name}"]'
        self.page.locator(selector).click()
    
    def cart_badge_count(self):
        badge = self.page.locator('[data-test="shopping-cart-badge"]')
        if badge.is_visible():
            return int(badge.inner_text())
        return 0

    def get_all_prices(self):
        return self.page.locator(".inventory_item_price").all_inner_texts()
    
    def get_price_for(self, product_name):
    
        items = self.page.locator(".inventory_item")
        count = items.count()
        for i in range(count):
            item = items.nth(i)
            name = item.locator(".inventory_item_name").inner_text()
            if name == product_name:
             return item.locator(".inventory_item_price").inner_text()
        return None                             