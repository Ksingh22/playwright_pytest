class CheckoutPage:

    def __init__(self,page): 
        self.page = page
        self._first_name = page.locator("#first-name")
        self._last_name = page.locator("#last-name")
        self._postcode = page.locator("#postal-code")
        self._continue_button = page.locator("#continue")
        self._finish_button = page.locator("#finish")
        self._confirm_message = page.locator("h2.complete-header")

    def enter_first_name(self,first_name):
        return self._first_name.fill(first_name)


    def enter_last_name(self,last_name):
        return self._last_name.fill(last_name)

    def enter_postcode(self,postcode):
        return self._postcode.fill(postcode)
    
    def enter_checkout_details(self,first,last,postcode):
        self.enter_first_name(first)
        self.enter_last_name(last)
        self.enter_postcode(postcode)
        return self
    
    def click_continue_button(self):
        self._continue_button.click()
        return self
 

    def click_finish_button(self):
        self._finish_button.click()
        return self
    
    def get_confirm_message(self):
        return self._confirm_message