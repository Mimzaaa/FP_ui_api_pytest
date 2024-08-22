from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage():
   def __init__(self, driver: WebDriver) -> None:
       self.__url = "https://www.chitai-gorod.ru/"
       self.__driver = driver

   def go(self):
       self.__driver.get(self.__url)