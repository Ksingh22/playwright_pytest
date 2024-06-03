import pytest
from src.pages.login_page import LoginPage

@pytest.fixture(scope="function")
def setUp(page):
    page.set_viewport_size({'width':1920, 'height':1020})
    page.goto("http://saucedemo.com")
    yield page