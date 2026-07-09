from selenium.webdriver.common.by import By


class OrderPageDetailsLocators:

    OFFER_PAGE_DETAIL_TITLE = (By.XPATH, ".//div[text()='Про аренду']")
    DATE_OFFER = (By.XPATH, ".//input[contains(@placeholder,'Когда привезти самокат')]")
    DATE_OFFER_LIST = (By.XPATH, ".//div[(@class='react-datepicker__week')]//div[@tabindex='0']")
    PERIOD_RENT = (By.CLASS_NAME, 'Dropdown-placeholder')
    PERIOD_RENT_LIST = ".//div[contains(@class,'Dropdown-option') and contains(text(),'{}')]"
    COMMENT_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_DOWN = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    TITLE = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    TITLE_ORDER = (By.XPATH, ".//div[text()='Заказ оформлен']")