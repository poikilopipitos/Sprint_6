import allure
from pages.header_links_page import HeaderLinkPage


class TestHeaderLinkPage:
    @allure.title('Проверка работы клика по ссылке самоката')
    def test_check_samokat_link(self, driver):
        header_link_page= HeaderLinkPage(driver)
        header_link_page.click_samokat_link()

        assert "qa-scooter.praktikum-services.ru" in driver.current_url

    @allure.title('Проверка работы клика по ссылке яндекса')
    def test_click_yandex_link(self, driver):
        header_link_page= HeaderLinkPage(driver)
        header_link_page.click_yandex_link()
        
        assert "dzen.ru" in driver.current_url