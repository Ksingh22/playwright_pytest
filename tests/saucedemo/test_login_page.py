from playwright.sync_api import expect
from src.pages.login_page import LoginPage


def test_login_with_standard_user(login) -> None:
    expect(login.product_header).to_be_visible()
    expect(login.product_header).to_have_text("Products")

def test_login_failure(setUp)-> None:
    page = setUp
    login_p = LoginPage(page)
    login_p.click_login_btn()
    expected_fail_message = "Username is required"
    expect(login_p.get_error_message).to_contain_text(expected_fail_message)


