import requests

class ApiReadCity:

    def __init__(self, base_url="https://web-gate.chitai-gorod.ru/api", city_id=213, token=None):
        self.base_url = base_url
        self.city_id = city_id
        self.token = token

    def get_headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
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
        return self.post(endpoint, data=data)
    
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