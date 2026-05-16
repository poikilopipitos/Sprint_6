from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage


class BasePage:
    
    OFFER_BUTTON_UP = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    TITLE_8 = (By.ID , 'accordion__heading-7')
    OFFER_BUTTON_DOWN = (By.XPATH, ".//div[contains(@class,'Home')]//button[text()='Заказать']")
    OFFER_TITLE = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_for_page_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_BUTTON_UP))

    def scroll_voprosi_title(self):
        self.wait_for_page_to_load()
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.TITLE_8))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_answer_text(self,index):
        self.scroll_voprosi_title()
        title_locator = (By.ID, f'accordion__heading-{index}')
        answer_locator = (By.ID, f'accordion__panel-{index}')
        self.wait.until(expected_conditions.visibility_of_element_located(title_locator)).click()

        answer_element = self.wait.until(expected_conditions.visibility_of_element_located(answer_locator))
        return answer_element.text

    def button_up_offer_click(self):
        self.wait_for_page_to_load()
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_BUTTON_UP)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_TITLE)) 

        return OrderPage(self.driver)

    def button_down_offer_click(self):
        self.wait_for_page_to_load()
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_BUTTON_DOWN))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_BUTTON_DOWN)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_TITLE))

        return OrderPage(self.driver)