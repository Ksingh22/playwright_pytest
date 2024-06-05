from playwright.sync_api import expect

class DemoPage:

    def __init__(self,page):
        self.page = page
        self._header_btns = page.locator("div.d-flex.web-menu-btn button").all()
        self._free_demo_btn = page.locator("#Form_getForm_action_submitForm")
        self._full_name = page.get_by_placeholder("Your Full Name*")
        self._phone_number = page.get_by_placeholder("Phone Number*")
        self._business_email = page.get_by_placeholder("Business Email*")
        self._country = page.get_by_label("Country")
        self._countries = page.locator("#Form_getForm_Country_Holder option").all()
        self._employee = page.get_by_label("No Of Employees")
        self._employees = page.locator("#Form_getForm_NoOfEmployees option").all()
        self._job_title = page.get_by_placeholder("Job Title*")
        self._message_box = page.get_by_placeholder("Your Message*")
        
    
    def click_header_bts(self,button_name): 
        for btn in self._header_btns:
            if btn.inner_text() == button_name:
                btn.click()
                break
    
    def free_demo_btn(self):
        return self._free_demo_btn

    def enter_full_name(self,full_name):
        self._full_name.fill(full_name)
    
    def enter_phone_number(self,ph_no):
        self._phone_number.fill(ph_no)
    
    def enter_business_email(self,email):
        self._business_email.fill(email)
    
    def select_country(self,country):
        self._country.select_option(country)
   
    def select_employee(self,employee):
        self._employee.select_option(employee)
    
    def enter_job_title(self,job_title):
        self._job_title.fill(job_title)
    
    def enter_message_box(self,message):
        self._message_box.fill(message)
