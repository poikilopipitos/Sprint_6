from pages.base_page import BasePage
import allure
import pytest
from data import BasePageData


class TestBasePage:
    
    @pytest.mark.parametrize("index, expected_answer, allure_title",BasePageData.QUESTIONS_AND_ANSWERS)
    def test_check_answers(self, driver, index, expected_answer, allure_title):
    
        allure.dynamic.title(allure_title)
        base_page = BasePage(driver)
        actual_answer = base_page.get_answer_text(index)
        
        assert actual_answer == expected_answer, f"Ошибка в вопросе с индексом {index}!"

