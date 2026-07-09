from selenium.webdriver.common.by import By


class OrderPageLocators:

    OFFER_TITLE = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")
    INPUT_FIRST_NAME = (By.XPATH, ".//input[contains(@placeholder,'Имя')]")
    INPUT_LAST_NAME = (By.XPATH, ".//input[contains(@placeholder,'Фамилия')]")
    ADDRESS = (By.XPATH, ".//input[contains(@placeholder,'Адрес: куда привезти заказ')]")
    SUBWAY = (By.XPATH, ".//input[contains(@placeholder,'Станция метро')]")
    SUBWAY_LIST_CLICK = ".//ul[@class='select-search__options']//div[text()='{}']"
    PHONE_NUMBER = (By.XPATH, ".//input[contains(@placeholder,'Телефон: на него позвонит курьер')]")
    FURTHER_BUTTON = (By.XPATH, ".//button[text()='Далее']")