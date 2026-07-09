from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_loaded(self):
        self.wait_for_page_to_load(MainPageLocators.OFFER_BUTTON_UP)

    def scroll_voprosi_title(self):
        self.scroll_element(MainPageLocators.TITLE_8)

    def click_answer_text(self, index):
        dynamic_id = MainPageLocators.QUESTION.format(index)
        locator = (By.ID, dynamic_id)
        self.click_on_element(locator)

    def get_answer_text(self, index):
        dynamic_id = MainPageLocators.ANSWER.format(index)
        locator = (By.ID, dynamic_id)
        return self.get_text(locator)
    
    def button_up_offer_click(self):
        self.click_on_element(MainPageLocators.OFFER_BUTTON_UP)
        
    def button_down_offer_click(self):
        self.scroll_element(MainPageLocators.OFFER_BUTTON_DOWN)
        self.click_on_element(MainPageLocators.OFFER_BUTTON_DOWN)
        
