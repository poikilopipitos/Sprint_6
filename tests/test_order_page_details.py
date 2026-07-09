import allure
import pytest
from pages.base_page import BasePage
from data.data import OrderPageDetailsData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_page_details import OrderPageDetails

@allure.feature('Страница деталей заказа')
class TestOrderPageDetails:

    @pytest.mark.parametrize('first_name, last_name, address, subway, phone, date, period, color, comment',OrderPageDetailsData.ORDER_DETAILS_DATA)
    @allure.title('Проверка оформления заказа')
    def test_offer_details(self,driver,first_name,last_name,address,subway,phone,date,period,color,comment):
        main_page = MainPage(driver)
        main_page.button_down_offer_click()
        order_page = OrderPage(driver)
        order_page.fill_first_order_step(first_name,last_name,address,subway,phone)
        order_page_details = OrderPageDetails(driver)
        order_page_details.complete_order_details_form(date,period,color,comment)
        
        assert order_page_details.order_header_visible() 







