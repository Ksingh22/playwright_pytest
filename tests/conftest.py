import pytest
from playwright.sync_api import  Playwright
from src.pages.login_page import LoginPage
# from fixtures.setup_fixture import setUp
# from fixtures.login_fixture import login
# from fixtures.logout_fixture import logout

@pytest.fixture(scope="function")
def setUp(page, playwright : Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://saucedemo.com")
    yield page
    browser.close()

@pytest.fixture(scope="function")
def login(setUp):
    page = setUp
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    product_p = login_p.login(credentials)
    return product_p
    
@pytest.fixture(scope="function")
def logout(setUp,login):
    page = setUp
    login_p = LoginPage(page)
    login.do_logout()
    return login_p

@pytest.fixture(scope="session")
def browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # create a new page inside context.
    page = context.new_page()
    page.goto("https://www.orangehrm.com/")
    yield page
    context.close()
    browser.close()   




