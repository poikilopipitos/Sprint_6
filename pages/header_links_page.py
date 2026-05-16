from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HeaderLinkPage:

    SAMOKAT_LOGO = (By.XPATH, ".//a[@href='/']")
    YANDEX_LINK = (By.XPATH, ".//a[@href='//yandex.ru']")
    DZEN_LOGO = (By.ID,'dzen-header')
    OFFER_TITLE = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")
    OFFER_BUTTON_UP = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    TITLE_BASE_PAGE = (By.XPATH, ".//div[contains(text(),'Привезём его прямо к вашей двери,')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_for_main_page_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_BUTTON_UP))

    def click_samokat_logo(self):
        self.driver.find_element(*self.OFFER_BUTTON_UP).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.OFFER_TITLE))
        self.wait.until(expected_conditions.visibility_of_element_located(self.SAMOKAT_LOGO)).click()
        return self.wait.until(expected_conditions.visibility_of_element_located(self.TITLE_BASE_PAGE))

    def click_yandex_logo(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.YANDEX_LINK))
        self.driver.find_element(*self.YANDEX_LINK).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def check_dzen_logo(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.DZEN_LOGO))


    def click_samokat_link(self):
        self.wait_for_main_page_load()
        self.click_samokat_logo()
        
    def click_yandex_link(self):
        self.wait_for_main_page_load()
        self.click_yandex_logo()
        self.check_dzen_logo()

