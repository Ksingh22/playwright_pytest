import pytest
from playwright.sync_api import expect
from src.pages.demo_page import DemoPage
from utils.helper import helper

data = helper

@pytest.mark.parametrize("test_case", data.get_test_data())
def test_demo_page_case(browser_context,test_case):
    page = browser_context 
    demo_p = DemoPage(page)
    data.loop_test_data(test_case, demo_p)
    expect(demo_p.free_demo_btn()).to_be_visible()

def test_demo_page_case1(browser_context):
    page = browser_context 
    demo_p = DemoPage(page)
    data.create_test_data(demo_p)
    expect(demo_p.free_demo_btn()).to_be_visible()

   

