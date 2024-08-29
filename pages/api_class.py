import requests
from configuration.ConfigProvider import ConfigProvider
import requests

class ApiReadCity:

    def __init__(self, config_provider: ConfigProvider):
        api_config = config_provider.get_api_config()
        self.base_url = api_config['base_url']
        self.city_id = api_config['city_id']
        self.token = api_config['token']

    def get_headers(self):
        headers = {}
        if self.token:
            headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
            }
        return headers

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response

    def search_product(self, phrase, page=1, per_page=10, sort="relevance"):
        endpoint = "/v2/search/product"
        params = {
            'customerCityId': self.city_id,
            'phrase': phrase,
            'products[page]': page,
            'products[per-page]': per_page,
            'sortPreset': sort
        }
        return self.get(endpoint, params=params)



    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response

    def add_bookmark(self, book_id):
        endpoint = "/v1/bookmarks"
        data = {"id": book_id}
        response = self.post(endpoint, data=data)
        return response



    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.delete(url, json=data, headers=headers)
        response.raise_for_status()
        return response
    
    def remove_bookmark(self, book_id):
        endpoint = "/v1/bookmarks/3026125"
        data = {"id": book_id}
        return self.delete(endpoint, data=data)
    


    def patch(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.patch(url, json=data, headers=headers)
        response.raise_for_status()
        return response

    def update_personal_data(self, personal_data):
        endpoint = "/v1/profile/personal-data"
        return self.patch(endpoint, data=personal_data)