import pytest
import allure
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get('https://www.chitai-gorod.ru/')
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
   
    with allure.step("Закрыть браузер"):
        browser.quit()