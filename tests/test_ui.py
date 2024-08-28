import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.ui_class import HomePage

import pytest
@pytest.mark.skip
@allure.title("Проверка работы поля 'Поиск'")
def test_search_functionality_val_1(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('проверка')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «проверка»" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поле 'Поиск' принимает данные на латинице")
def test_search_functionality_val_2(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('the miracle morning')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «the miracle morning»" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поле 'Поиск' принимает данные состоящие из 2 букв")
def test_search_functionality_val_3(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('ид')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «bl»" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поле 'Поиск' принимает данные с пропущенной буквой")
def test_search_functionality_val_4(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('рвизор')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «ревизор»" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поле 'Поиск' принимает данные с символом на конце запроса")
def test_search_functionality_val_5(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('ревизор!')
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «ревизор»" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поле 'Поиск' не принимает данные, состоящие из двух слов без пробела")
def test_search_functionality_neg_1(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('николайгоголь')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Похоже, у нас такого нет" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поле 'Поиск' не принимает данные, состоящие из одной буквы")
def test_search_functionality_neg_2(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('и')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    
    with allure.step("Результат: " + result_message):
        assert "Похоже, у нас такого нет" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поиск товара с помощью символов")
def test_search_functionality_neg_3(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('@#$%^&')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    
    with allure.step("Результат: " + result_message):
        assert "Похоже, у нас такого нет" in result_message, "Текст не соответствует ожидаемому"

@pytest.mark.skip
@allure.title("Поиск товара с пустым полем")
def test_search_functionality_neg_4(browser:  WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('')
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert result_message == "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."

@pytest.mark.skip
@allure.title("Поиск товара с данными из пробелов")
def test_search_functionality_neg_5(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.go()
    home_page.search('' * 5)
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert result_message == "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."