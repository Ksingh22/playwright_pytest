import json
from faker import Faker

data_generator = Faker()

class helper:
    def __init__(self):
          self._ = None

    def get_test_data():
            test_data = []
            with open("utils/test_data.json") as data_file:    
                data = json.load(data_file)
                for v in data.values():
                    test_data.append(v)
            return test_data
    # using test data from json test file
    def loop_test_data(test_data,page):
        page.click_header_bts("Contact Sales")
        page.enter_full_name(test_data["full_name"])
        page.enter_phone_number(test_data["phone_number"])
        page.enter_business_email(test_data["business_email"])
        page.select_country(test_data["country"])
        page.select_employee(test_data["employee"])
        page.enter_job_title(test_data["job_title"])
        page.enter_message_box(test_data["message_box"])
    
    # create a test data using faker library
    def create_test_data(page):
        page.click_header_bts("Contact Sales")
        page.enter_full_name(data_generator.name())
        page.enter_phone_number(data_generator.phone_number())
        page.enter_business_email(data_generator.email())
        page.select_country(data_generator.country())
        page.select_employee("11 - 15")
        page.enter_job_title(data_generator.job())
        page.enter_message_box(data_generator.text(max_nb_chars=80))
