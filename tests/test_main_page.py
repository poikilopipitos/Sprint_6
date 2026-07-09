from pages.order_page import OrderPage
import allure
import pytest
from data.data import BasePageData
from pages.main_page import MainPage


class TestMainPage:
    
    @pytest.mark.parametrize("index, expected_answer, allure_title",BasePageData.QUESTIONS_AND_ANSWERS)
    def test_check_answers(self,driver, index, expected_answer, allure_title):
        allure.dynamic.title(allure_title)
        main_page = MainPage(driver)
        main_page.scroll_voprosi_title()
        main_page.click_answer_text(index)
        actual_answer = main_page.get_answer_text(index)
        
        assert actual_answer == expected_answer, f"Ошибка в вопросе с индексом {index}!"

    @allure.title('Проверка входа в сценарий, через верхнюю кнопку')
    def test_button_up_offer_click(self,driver):
        main_page = MainPage(driver)
        main_page.button_up_offer_click()
        order_page = OrderPage(driver)
        assert order_page.order_page_is_header_visible() 

    @allure.title('Проверка входа в сценарий, через нижнюю кнопку')
    def test_button_down_offer_click(self,driver):
        main_page = MainPage(driver)
        main_page.button_down_offer_click()
        order_page = OrderPage(driver)
        assert order_page.order_page_is_header_visible() 

        