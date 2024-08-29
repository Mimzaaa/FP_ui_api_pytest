import pytest
import allure
from selenium import webdriver
from pages.api_class import ApiReadCity
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.maximize_window()
        yield browser
   
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def config_provider():
    return ConfigProvider()

@pytest.fixture
def data_provider():
    return DataProvider()

@pytest.fixture
def api_client(config_provider):
    return ApiReadCity(config_provider)

@pytest.fixture()
def test_data():
    return DataProvider()