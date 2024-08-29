import configparser

global_config = configparser.ConfigParser()
global_config.read('test_config.ini')


class ConfigProvider:

    def __init__(self) -> None:
        self.config = global_config

    def get_api_config(self):
        return {
            'base_url': self.config['test_api']['base_url'],
            'city_id': int(self.config['test_api']['city_id']),
            'token': self.config['test_api']['token']
        }

    def get_ui_config(self):
        return {
            'homepage_url': self.config['test_ui']['homepage_url']
        }