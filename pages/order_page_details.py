from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_details_locators import OrderPageDetailsLocators


class OrderPageDetails(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def order_page_details_is_header_visible(self):
        return self.is_element_present(OrderPageDetailsLocators.OFFER_PAGE_DETAIL_TITLE)

    def wait_for_order_details_load_page(self):
        self.wait_for_page_to_load(OrderPageDetailsLocators.OFFER_PAGE_DETAIL_TITLE)

    def set_date_offer(self, date):
        self.set_text(OrderPageDetailsLocators.DATE_OFFER,date)
        self.click_on_element(OrderPageDetailsLocators.DATE_OFFER_LIST)
  
    def set_period_rent(self, period_rent):
        self.click_on_element(OrderPageDetailsLocators.PERIOD_RENT)
        xpath = OrderPageDetailsLocators.PERIOD_RENT_LIST.format(period_rent)
        locator = (By.XPATH,xpath)
        self.click_on_element(locator)

    def set_color(self, color_name):
        locator = (By.ID,color_name)
        self.click_on_element(locator )

    def set_comment_courier(self,comment_courier):
        self.set_text(OrderPageDetailsLocators.COMMENT_COURIER,comment_courier)
        
    def click_order_button_down(self):
        self.click_on_element(OrderPageDetailsLocators.ORDER_BUTTON_DOWN)
        
    def wait_offer_title(self):
        self.is_header_visible(OrderPageDetailsLocators.TITLE)

    def click_button_yes(self):
        self.click_on_element(OrderPageDetailsLocators.BUTTON_YES)
       
    def wait_order_title(self):
        self.is_header_visible(OrderPageDetailsLocators.TITLE_ORDER)

    def complete_order_details_form(self,date,period_rent,color_name,comment_courier):
        self.wait_for_order_details_load_page()
        self.set_date_offer(date)
        self.set_period_rent(period_rent)
        self.set_color(color_name)
        self.set_comment_courier(comment_courier)
        self.click_order_button_down()
        self.wait_offer_title()
        self.click_button_yes()
        
    def order_header_visible(self):
        return self.is_element_present(OrderPageDetailsLocators.TITLE_ORDER)
        
        