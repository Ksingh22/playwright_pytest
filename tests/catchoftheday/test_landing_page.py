from playwright.sync_api import expect
from src.pages.landing_page import LandingPage

"""
This test clicks on EOFY Sale header link
and verifies that the header is visible

"""
def test_landing_page(open_catch_url):
    page = open_catch_url 
    landing_p = LandingPage(page)
    landing_p.click_header_links("EOFY Sale")
    expect(landing_p._header_verify).to_be_visible()

    """
    This test adds three random products from deal page
    and checkout

    """
def test_add_deal_to_cart(open_catch_url):
    page = open_catch_url 
    landing_p = LandingPage(page)
    landing_p.click_header_links("EOFY Sale")
    landing_p.click_deal(1)
    landing_p.click_deals_from_filter("Catch")
    products_to_add = 3
    landing_p.add_random_products_to_cart(products_to_add)
    landing_p.click_cart_icon()
    expect(landing_p._shopping_cart_title).to_be_visible()
    

