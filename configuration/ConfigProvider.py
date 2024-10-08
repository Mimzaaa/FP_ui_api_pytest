import configparser
import allure
"""Загружаем глобальную конфигурацию из файла 'test_config.ini'."""
global_config = configparser.ConfigParser()
global_config.read('test_config.ini')


class ConfigProvider:
    """
    Класс для предоставления конфигурации API и UI.
    Атрибуты:
        config (ConfigParser): Объект конфигурации.
    Методы:
        get_api_config() -> dict: Возвращает конфигурацию API.
        get_ui_config() -> dict: Возвращает конфигурацию UI.
    """
    def __init__(self) -> None:
        self.config = global_config

   
    @allure.step("Получить конфигурацию API")
    def get_api_config(self):
        """:return: Словарь с конфигурацией API (base_url, city_id, token)."""
        return {
            'base_url': self.config['test_api']['base_url'],
            'city_id': int(self.config['test_api']['city_id']),
            'token': self.config['test_api']['token']
        }

    
    @allure.step("Получить конфигурацию UI")
    def get_ui_config(self):
        """return: Словарь с конфигурацией UI (homepage_url)."""
        return {
            'homepage_url': self.config['test_ui']['homepage_url']
        }