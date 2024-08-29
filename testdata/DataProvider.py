import json

my_file = open('test_data.json')

global_data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get_search_tests(self):
        return self.data.get('search_tests', [])

    def get_personal_data_tests(self):
        return [self.data.get('personal_data', {})]
    
    def get_search_data(self):
        return self.data['search_data']
    
    def get_book_id(self):
        return self.data['book_id']