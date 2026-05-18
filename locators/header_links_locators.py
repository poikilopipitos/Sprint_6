from selenium.webdriver.common.by import By


class HeaderLinksLocators:

    SAMOKAT_LOGO = (By.XPATH, ".//a[@href='/']")
    YANDEX_LINK = (By.XPATH, ".//a[@href='//yandex.ru']")
    OFFER_TITLE = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")
    OFFER_BUTTON_UP = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    TITLE_BASE_PAGE = (By.XPATH, ".//div[contains(text(),'Привезём его прямо к вашей двери,')]")