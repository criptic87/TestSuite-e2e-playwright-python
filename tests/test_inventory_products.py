from playwright.sync_api import expect
"""
def test_add_cart(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")
"""