import random

class LandingPage:
    
    def __init__(self, page):
        self.page = page
        self._header_links = page.locator(".css-4hbenv div a").all()
        self._header_verify = page.locator(".event--title h1")
        self._get_all_deals = page.locator(".event.event--single div.event--card").all()
        self._cart_icon = page.locator("#mini-cart")
        self._cart_items = page.locator("ul[aria-label='Items from Catch'] li").all()
        self._popup_window = page.locator(".modal-content")
        self._added_to_cart_popup = page.locator(".toast.toast-success .message")
        self._shopping_cart_title = page.locator("h1.css-lnirao.e12cshkt0")
              
    def click_header_links(self,link_name): 
        for link in self._header_links:
            if link.inner_text() == link_name:
                link.click()
                break

    def get_header_text(self):
        return self._header_verify
    
    def click_deal(self,event):
        get_all_deals = self.page.locator(".event.event--single div.event--card").nth(event)
        get_all_deals.click()
    
    # two filter names, Catch and Marketplace 
    def get_deals_from_filter_locator(self, deals_from):
        return self.page.locator(f"//label[@title='{deals_from}']")
    
    def click_deals_from_filter(self,deals_from):
        self.get_deals_from_filter_locator(deals_from).click()
    
    # def click_deals_from_filter(self,deals_from):
    #     if len(self._popup_window) > 0:
    #         self.page.locator("#dobFormAccept").click()
    #     else:
    #         self.get_deals_from_filter_locator(deals_from).click()

    def get_products_locator(self):
        return self.page.locator(".product--card").all()

    def add_random_products_to_cart(self,number_of_products):
        random_products = random.choices(self.get_products_locator(), k=number_of_products)
        for product in random_products:
            product.hover()
            product.wait_for()
            product.locator("button").click()
            self.page.wait_for_selector(".toast.toast-success .message").wait_for_element_state("stable")

    def click_cart_icon(self):
        self.page.wait_for_selector("#mini-cart").wait_for_element_state("stable")
        self._cart_icon.click()
    
    def get_shopping_cart_title(self):
        return self._shopping_cart_title
    

        
       
