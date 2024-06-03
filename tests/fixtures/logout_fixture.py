import pytest
from src.pages.login_page import LoginPage

@pytest.fixture(scope="function")
def logout(setUp,login,page):
    login_p = LoginPage(page)
    login.do_logout()
    return login_p