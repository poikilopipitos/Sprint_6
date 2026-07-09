import allure
from pages.header_links_page import HeaderLinkPage
from pages.main_page import MainPage
from config.constants import Urls


class TestHeaderLinkPage:
    @allure.title('Проверка работы клика по ссылке самоката')
    def test_check_samokat_link(self, driver):
        main_page = MainPage(driver)
        main_page.button_up_offer_click()
        header_link_page= HeaderLinkPage(driver)
        header_link_page.click_samokat_logo()

        assert Urls.SAMOKAT_MAIN_URL in header_link_page.get_current_url()

    @allure.title('Проверка работы клика по ссылке яндекса')
    def test_click_yandex_link(self, driver):
        header_link_page= HeaderLinkPage(driver)
        header_link_page.click_yandex_logo()
        header_link_page.switch_to_new_window()

        assert Urls.YANDEX_DZEN_URL in header_link_page.get_current_url()