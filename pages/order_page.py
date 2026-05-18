from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators


class OrderPage(BasePage):
   
    def __init__(self, driver):
        super().__init__(driver)

    def order_page_is_header_visible(self):
        return self.is_element_present(OrderPageLocators.OFFER_TITLE)

    def wait_for_order_load_page(self):
        self.wait_for_page_to_load(OrderPageLocators.OFFER_TITLE)

    def set_first_name(self,first_name):
        self.set_text(OrderPageLocators.INPUT_FIRST_NAME,first_name)
        
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.INPUT_LAST_NAME,last_name)

    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS,address)

    def set_subway(self, subway):
        self.click_on_element(OrderPageLocators.SUBWAY)
        self.set_text(OrderPageLocators.SUBWAY,subway)
        current_xpath = OrderPageLocators.SUBWAY_LIST_CLICK.format(subway)
        locator = (By.XPATH,current_xpath)
        self.wait_element_to_be_clickable(locator)
        self.click_on_element(locator)

    def set_phone_number(self, phone_number):
        self.set_text(OrderPageLocators.PHONE_NUMBER,phone_number)
  
    def click_further_button(self):
        self.wait_visibility_of_element_located(OrderPageLocators.FURTHER_BUTTON)
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    def fill_first_order_step(self,first_name,last_name,address,subway,phone_number):
        self.wait_for_order_load_page()
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_subway(subway)
        self.set_phone_number(phone_number)
        self.click_further_button()
