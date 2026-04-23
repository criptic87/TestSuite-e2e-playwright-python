from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login(login_page, inventory_page,  test_users):
    user = test_users["valid_user"]
    login_page.login(user["username"], user["password"])
    expect(inventory_page.shopping_cart).to_be_visible()
    
def test_fail_login(login_page, test_users):
    user = test_users["invalid_user"]
    login_page.login(user["username"], user["password"])
    expect(login_page.error_message_text).to_contain_text("Username and password do not matc")
    expect(login_page.error_button_close).to_be_visible()

def test_fail_close_error_try_again_success(login_page, inventory_page, test_users):
    login_page.login("stan", "secret_sauce")
    expect(login_page.error_message_text).to_contain_text("Username and password do not match")

    login_page.error_button_close.click()
    user = test_users["valid_user"]
    login_page.login(user["username"], user["password"])
    expect(inventory_page.shopping_cart).to_be_visible()

def test_no_password_login(login_page):
    login_page.login("standard_user", "")
    expect(login_page.error_message_text).to_contain_text("Password is required")

def test_no_username_login(login_page):
    login_page.login("", "secret_sauce")
    expect(login_page.error_message_text).to_contain_text("Username is required")

def test_locked_user_login(login_page, test_users):
    user = test_users["locked_out_user"]
    login_page.login(user["username"], user["password"])
    expect(login_page.error_message_text).to_contain_text("user has been locked out.")

def test_redirect_to_login_if_not_auth(login_page, page):
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/", timeout=5000)
    expect(login_page.error_message_text).to_contain_text("You can only access '/inventory.html' when you are logged")

def test_session_persists_on_refresh(logged_in_inventory, page):
    page.reload()
    logged_in_inventory.should_be_loaded()

def test_cannot_access_inventory_after_logout(logged_in_inventory, page):
    logged_in_inventory.logout()
    logged_in_inventory.navigate()
    LoginPage(page).should_be_on_login_page()

"""
def test_problem_user_login(login_page, test_users, inventory_page):
    user = test_users["problem_user"]
    login_page.login(user["username"], user["password"])
    expect(inventory_page)
"""
