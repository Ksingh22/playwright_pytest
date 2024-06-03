from src.pages.products_page import ProductListPage

class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._error_message = page.locator("//h3[@data-test='error']")

    def enter_username(self, username):
        self._username.fill(username)
    
    def enter_password(self, password):
        self._password.fill(password)

    def click_login_btn(self):
        self._login_btn.click()

    def login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login_btn()
        return ProductListPage(self.page)
    
    @property
    def get_error_message(self):
        return self._error_message
    
    @property
    def login_button(self):
        return self._login_btn