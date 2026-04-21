from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message_text = page.locator('[data-test="error"]')
        self.error_button_close = page.locator('[data-test="error-button"]')

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def should_be_on_login_page(self):
        expect(self.page).to_have_url(self.url)
        expect(self.username_input).to_be_visible()

    @property
    def error_message(self):
        return self.error_message_text
