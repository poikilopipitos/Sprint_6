from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_for_page_to_load(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def scroll_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self,locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    def is_header_visible(self,locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
        
    def click_on_element(self,locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def set_text(self,locator,text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)
    
    def wait_element_to_be_clickable(self,locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_of_element_located(self,locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def switch_to_new_window(self, expected_windows_count=2):
        self.wait.until(expected_conditions.number_of_windows_to_be(expected_windows_count))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 20).until(expected_conditions.url_contains("dzen"))
    def get_current_url(self):
        return self.driver.current_url
    
    def is_element_present(self, locator):
       
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0