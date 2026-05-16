import allure
import pytest
from pages.base_page import BasePage
from data import OrderPageData


class TestOrderPage:

    @pytest.mark.parametrize('first_name, last_name, address, subway, phone',OrderPageData.ORDER_USER_DATA)
    @allure.title('Проверка входа в сценарий, через верхнюю кнопку')
    def test_offer_up(self, driver,first_name,last_name,address,subway,phone):
        base_page = BasePage(driver)
        order_page = base_page.button_up_offer_click()
        order_page_details = order_page.offer(first_name,last_name,address,subway,phone)

        assert order_page_details.wait_for_order_details_load_page().text == "Про аренду"

    @pytest.mark.parametrize('first_name, last_name, address, subway, phone',OrderPageData.ORDER_USER_DATA)
    @allure.title('Проверка входа в сценарий, через нижнюю кнопку')
    def test_offer_down(self, driver,first_name,last_name,address,subway,phone):
        base_page = BasePage(driver)
        order_page = base_page.button_down_offer_click()
        order_page_details = order_page.offer(first_name,last_name,address,subway,phone)

        assert order_page_details.wait_for_order_details_load_page().text == "Про аренду"


        