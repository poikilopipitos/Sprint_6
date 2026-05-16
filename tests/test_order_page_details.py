import allure
import pytest
from pages.base_page import BasePage
from data import OrderPageDetailsData


@allure.feature('Страница деталей заказа')
class TestOrderPageDetails:

    @pytest.mark.parametrize('first_name, last_name, address, subway, phone, date, period, color, comment',OrderPageDetailsData.ORDER_DETAILS_DATA)
    @allure.title('Проверка оформления заказа')
    def test_offer_details(self,driver,first_name,last_name,address,subway,phone,date,period,color,comment):
        base_page = BasePage(driver)
        order_page = base_page.button_down_offer_click()
        order_page_details = order_page.offer(first_name,last_name,address,subway,phone)
        order_page_details.offer_details(date,period,color,comment)
        assert "Заказ оформлен" in order_page_details.wait_order_title().text





