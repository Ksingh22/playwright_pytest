from playwright.sync_api import expect
from faker import Faker

data_generator = Faker()

def test_add_to_cart(login) -> None:
    product_name = "Sauce Labs Bolt T-Shirt"
    product_p = login
    product_p.click_add_to_cart_or_remove(product_name) 

def test_remove_product_from_cart(login) -> None:
    product_name = "Sauce Labs Bolt T-Shirt"
    login.click_add_to_cart_or_remove(product_name)
    login.click_add_to_cart_or_remove(product_name)
    expect(login.get_add_remove_cart_locator(product_name)).to_have_text("Add to cart")

def test_checkout_process(login) -> None:
    product_name = "Sauce Labs Bolt T-Shirt"
    product_p = login
    product_p.click_add_to_cart_or_remove(product_name)
    
    expect(product_p.get_add_remove_cart_locator(product_name)).to_have_text("Remove")
    checkout_p= product_p.click_cart_icon()\
                        .click_checkout_btn()\
                        .enter_checkout_details(data_generator.file_name(),data_generator.last_name(),data_generator.zipcode())\
                        .click_continue_button()\
                        .click_finish_button()
    expect(checkout_p.get_confirm_message()).to_have_text("Thank you for your order!")