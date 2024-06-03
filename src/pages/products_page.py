from src.pages.carts_page import CartPage
class ProductListPage:

    def __init__(self,page):
        self.page = page
        self._product_header = page.locator("span.title")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")
        self._cart_icon = page.locator(".shopping_cart_link")
    
    @property
    def product_header(self):
        return self._product_header
    
    def click_burger_menu(self):
        self._burger_menu.click()
    
    def click_logout_btn(self):
        self._logout_btn.click()
    
    def do_logout(self):
        self.click_burger_menu()
        self.click_logout_btn()
    
    def get_add_remove_cart_locator(self, product):
        return self.page.locator(f"//div[text()='{product}']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button")
    
    def click_add_to_cart_or_remove(self,product):
        self.get_add_remove_cart_locator(product).click()
    
    def click_cart_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)
    

    