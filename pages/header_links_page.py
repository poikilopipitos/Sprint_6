from pages.base_page import BasePage
from locators.header_links_locators import HeaderLinksLocators


class HeaderLinkPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_main_page_load(self):
        self.wait_for_page_to_load(HeaderLinksLocators.OFFER_BUTTON_UP)
       
    def click_samokat_logo(self):
        self.click_on_element(HeaderLinksLocators.SAMOKAT_LOGO)
        
    def click_yandex_logo(self):
        self.click_on_element(HeaderLinksLocators.YANDEX_LINK)
     


