import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.ui_class import HomePage


def test_search_functionality_1(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search('проверка')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="search-page__found-message"]').text
    assert "Показываем результаты по запросу" in found_message

def test_search_functionality_2(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search('the miracle morning')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="search-page__found-message"]').text
    assert "Показываем результаты по запросу" in found_message

def test_search_functionality_3(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search('ид')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="search-page__found-message"]').text
    assert "Показываем результаты по запросу" in found_message

def test_search_functionality_4(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search('рвизор')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="search-page__found-message"]').text
    assert "Показываем результаты по запросу" in found_message

def test_search_functionality_5(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search('ревизор!')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="search-page__found-message"]').text
    assert "Показываем результаты по запросу" in found_message




def test_search_functionality_6(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search_neg('николайгоголь')
    
    found_message = browser.find_element(By.CSS_SELECTOR, '[class="catalog-empty-result__header"]').text
    assert "Похоже, у нас такого нет" in found_message

def test_search_functionality_7(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search_neg('и')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="catalog-empty-result__header"]').text
    assert "Похоже, у нас такого нет" in found_message

def test_search_functionality_8(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search_neg('@#$%^&')

    found_message = browser.find_element(By.CSS_SELECTOR, '[class="catalog-empty-result__header"]').text
    assert "Похоже, у нас такого нет" in found_message
 
def test_search_functionality_9(browser:  WebDriver):
    home_page = HomePage(browser)
    home_page.search_ver('')

    assert browser.current_url == "https://www.chitai-gorod.ru/"

def test_search_functionality_10(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.search_gaps('' * 5)

    assert browser.current_url == "https://www.chitai-gorod.ru/"