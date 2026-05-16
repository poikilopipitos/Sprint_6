from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page_details import OrderPageDetails


class OrderPage:
    OFFER_TITLE = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")
    INPUT_FIRST_NAME = (By.XPATH, ".//input[contains(@placeholder,'Имя')]")
    INPUT_LAST_NAME = (By.XPATH, ".//input[contains(@placeholder,'Фамилия')]")
    ADDRESS = (By.XPATH, ".//input[contains(@placeholder,'Адрес: куда привезти заказ')]")
    SUBWAY = (By.XPATH, ".//input[contains(@placeholder,'Станция метро')]")
    SUBWAY_LIST_CLICK = ".//ul[@class='select-search__options']//div[text()='{}']"
    PHONE_NUMBER = (By.XPATH, ".//input[contains(@placeholder,'Телефон: на него позвонит курьер')]")
    FURTHER_BUTTON = (By.XPATH, ".//button[text()='Далее']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_for_order_load_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_TITLE))

    def set_first_name(self,first_name):
        self.driver.find_element(*self.INPUT_FIRST_NAME).send_keys(first_name)
        
    def set_last_name(self, last_name):
        self.driver.find_element(*self.INPUT_LAST_NAME).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def set_subway(self, subway):
        self.driver.find_element(*self.SUBWAY).click()
        self.driver.find_element(*self.SUBWAY).send_keys(subway)
        current_xpath = self.SUBWAY_LIST_CLICK.format(subway)
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, current_xpath))).click()
  
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)
  
    def click_further_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.FURTHER_BUTTON))
        self.driver.find_element(*self.FURTHER_BUTTON).click() 
        return OrderPageDetails(self.driver)


    def offer(self,first_name,last_name,address,subway,phone_number):
        self.wait_for_order_load_page()
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_subway(subway)
        self.set_phone_number(phone_number)
        
        return self.click_further_button()
