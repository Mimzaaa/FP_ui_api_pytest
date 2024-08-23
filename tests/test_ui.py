import pytest
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.ui_class import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@allure.step("Проверка работы поля - Поиск")
def test_search_functionality_1(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('проверка')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Показываем результаты по запросу" in result_message

@allure.step("Поле принимает данные на латинице")
def test_search_functionality_2(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('the miracle morning')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message

@allure.step("Поле осуществляет поиск товара, состоящего из 2 букв")
def test_search_functionality_3(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('ид')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message

@allure.step("Поле осуществляет поиск товара с пропущенной буквой")
def test_search_functionality_4(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('рвизор')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message

@allure.step("Поле осуществляет поиск товара с символом на конце запроса")
def test_search_functionality_5(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('ревизор!')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message



@allure.step("Поиск товара, состоящего из двух слов без пробела")
def test_search_functionality_6(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('николайгоголь')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message

@allure.step("Поиск товара, состоящего из одной буквы")
def test_search_functionality_7(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('и')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message

@allure.step("Поиск товара с помощью символов")
def test_search_functionality_8(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('@#$%^&')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    with allure.step("Открывается страница с результатом поиска - "):
        assert result_message, "Похоже, у нас такого нет" in result_message
 
@allure.step("Поиск товара с пустым полем")
def test_search_functionality_9(browser:  WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    with allure.step("Открывается страница с результатом поиска"):
        assert result_message == "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."

@allure.step("Поиск товара с данными из пробелов")
def test_search_functionality_10(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('' * 5)
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    with allure.step("Открывается страница с результатом поиска"):
        assert result_message == "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."