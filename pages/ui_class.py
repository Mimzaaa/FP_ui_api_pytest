import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.chitai-gorod.ru/"
        self.__driver = driver

    @allure.step("Открыть страницу в браузере")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Ввести данные в поисковую строку")
    def search(self, query):
        self.__driver.find_element(By.CSS_SELECTOR, 'input[enterkeyhint="search"]').send_keys(query)
    
    @allure.step("Нажать на кнопку поиска")
    def click_search_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Искать"]').click()
    
    @allure.step("Получить сообщение с результатом поиска")
    def get_search_result_message(self) -> str:
        try:
            element_1 = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="search-page__found-message"]')))
            return element_1.text
        except TimeoutException:
            try:
                element_2 = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="catalog-empty-result__header"]')))
                return element_2.text
            except TimeoutException:
                return "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."