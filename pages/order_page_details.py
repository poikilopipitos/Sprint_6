from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPageDetails:

    OFFER_PAGE_DETAIL_TITLE = (By.XPATH, ".//div[text()='Про аренду']")
    FURTHER_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DATE_OFFER = (By.XPATH, ".//input[contains(@placeholder,'Когда привезти самокат')]")
    DATE_OFFER_LIST = (By.XPATH, ".//div[(@class='react-datepicker__week')]//div[@tabindex='0']")
    PERIOD_RENT = (By.CLASS_NAME, 'Dropdown-placeholder')
    PERIOD_RENT_LIST = ".//div[contains(@class,'Dropdown-option') and contains(text(),'{}')]"
    PERIOD_RENT_CONTROL = (By.XPATH, ".//div[@class='Dropdown-control']")
    COMMENT_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_UP = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_DOWN = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    TITLE = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    TITLE_ORDER = (By.XPATH, ".//div[text()='Заказ оформлен']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_for_order_details_load_page(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_PAGE_DETAIL_TITLE))

    def set_date_offer(self, date):
        self.driver.find_element(*self.DATE_OFFER).send_keys(date)
        date_offer_list = self.driver.find_element(*self.DATE_OFFER_LIST)
        date_offer_list.click()
  
    def set_period_rent(self, period_rent):
        self.driver.find_element(*self.PERIOD_RENT).click()
        xpath = self.PERIOD_RENT_LIST.format(period_rent)
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath))).click()

    def set_color(self, color_name):
        color_locator = (By.ID,color_name)
        self.driver.find_element(*color_locator).click()

    def set_comment_courier(self,comment_courier):
        self.driver.find_element(*self.COMMENT_COURIER).send_keys(comment_courier)

    def click_order_button_up(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.ORDER_BUTTON_UP)).click()
        
    def click_order_button_down(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.ORDER_BUTTON_DOWN)).click()
        
    def wait_offer_title(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.TITLE))

    def click_button_yes(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.BUTTON_YES)).click()
       
    def wait_order_title(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.TITLE_ORDER))


    def offer_details(self,date,period_rent,color_name,comment_courier):
        self.wait_for_order_details_load_page()
        self.set_date_offer(date)
        self.set_period_rent(period_rent)
        self.set_color(color_name)
        self.set_comment_courier(comment_courier)
        self.click_order_button_down()
        self.wait_offer_title()
        self.click_button_yes()
        

        