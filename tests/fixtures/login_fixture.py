import pytest
from src.pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login(setUp,page):
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    product_p = login_p.login(credentials)
    return product_p