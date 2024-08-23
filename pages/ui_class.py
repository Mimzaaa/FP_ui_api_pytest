from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.chitai-gorod.ru/"
        self.__driver = driver
    
    def go(self):
        self.__driver.get(self.__url)
    
    def search(self, query):
        self.__driver.find_element(By.CSS_SELECTOR, 'input[enterkeyhint="search"]').send_keys(query)
        self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Искать"]').click()
        
        WebDriverWait(self.__driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="search-page__found-message"]')))

    def search_neg(self, query):
        self.__driver.find_element(By.CSS_SELECTOR, 'input[enterkeyhint="search"]').send_keys(query)
        self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Искать"]').click()

        WebDriverWait(self.__driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="catalog-empty-result__header"]')))
    
    def search_ver(self, query):
        search_input = WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[enterkeyhint="search"]')))
        search_input.clear()
 
        search_button = WebDriverWait(self.__driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Искать"]')))
        search_button.click()

        WebDriverWait(self.__driver, 20).until(EC.url_to_be(self.__url))

    def search_gaps(self, query):
        search_input = WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[enterkeyhint="search"]')))
        search_input.send_keys(query)
 
        search_button = WebDriverWait(self.__driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Искать"]')))
        search_button.click()

        WebDriverWait(self.__driver, 10).until(EC.url_to_be(self.__url))