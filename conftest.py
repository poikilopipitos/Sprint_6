import pytest
from selenium import webdriver
from config.constants import Urls



@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()