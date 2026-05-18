from selenium.webdriver.common.by import By


class MainPageLocators:
    OFFER_BUTTON_UP = (By.XPATH, ".//div[contains(@class, 'Header')]//button[text()='Заказать']")
    TITLE_8 = (By.ID , 'accordion__heading-7')
    OFFER_BUTTON_DOWN = (By.XPATH, ".//div[contains(@class,'Home')]//button[text()='Заказать']")
    OFFER_TITLE = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")

    QUESTION = 'accordion__heading-{}'
    ANSWER = 'accordion__panel-{}'

