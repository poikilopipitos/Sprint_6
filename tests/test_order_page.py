import allure
import pytest
from data.data import OrderPageData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_page_details import OrderPageDetails

class TestOrderPage:

    @pytest.mark.parametrize('first_name, last_name, address, subway, phone',OrderPageData.ORDER_USER_DATA)
    @allure.title('Проверка входа в сценарий, через верхнюю кнопку')
    def test_offer_up(self, driver,first_name,last_name,address,subway,phone):
        main_page = MainPage(driver)
        main_page.button_up_offer_click()
        order_page = OrderPage(driver)
        order_page.fill_first_order_step(first_name,last_name,address,subway,phone)
        order_page_details = OrderPageDetails(driver)
        assert order_page_details.order_page_details_is_header_visible() 

    @pytest.mark.parametrize('first_name, last_name, address, subway, phone',OrderPageData.ORDER_USER_DATA)
    @allure.title('Проверка входа в сценарий, через нижнюю кнопку')
    def test_offer_down(self, driver,first_name,last_name,address,subway,phone):
        main_page = MainPage(driver)
        main_page.button_down_offer_click()
        order_page = OrderPage(driver)
        order_page.fill_first_order_step(first_name,last_name,address,subway,phone)
        order_page_details = OrderPageDetails(driver)

        assert order_page_details.order_page_details_is_header_visible() 


        