from playwright.sync_api import expect
from src.pages.login_page import LoginPage


# def test_login_with_standard_user(setUp) -> None:
#     page = setUp
#     credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
#     login_p = LoginPage(page)
#     product_p = login_p.login(credentials)
#     product_p.do_logout()
#     expect(login_p._login_btn).to_be_visible()
   

def test_login_with_standard_user(logout) -> None:
    expect(logout._login_btn).to_be_visible()