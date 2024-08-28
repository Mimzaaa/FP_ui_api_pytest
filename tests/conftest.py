import pytest
import allure
from selenium import webdriver
from pages.api_class import ApiReadCity

@pytest.fixture(scope="module")
def api_client():
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjEwNDQxOTU4LCJpYXQiOjE3MjQ4NTA1NjgsImV4cCI6MTcyNDg1NDE2OCwidHlwZSI6MjB9.cQCiI37drxMQ4wYlbyNP9FzWX78tUQcBjhYRVFPBa0k"
    return ApiReadCity(token=token)

@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.maximize_window()
        yield browser
   
    with allure.step("Закрыть браузер"):
        browser.quit()