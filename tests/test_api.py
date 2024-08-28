import pytest
import requests
from pages.api_class import ApiReadCity

def test_search_product(api_client: ApiReadCity):
    response = api_client.search_product("ревизор")
    json_response = response.json()

    assert response.status_code == 200, f"Ожидаемый код статус 200, но получили {response.status_code}"

    transformed_phrase = json_response['data']['attributes'].get('transformedPhrase', '').lower()
    assert 'ревизор' in transformed_phrase, f"Ожидаем 'ревизор' в transformedPhrase, но получили '{transformed_phrase}'"

    products = json_response['data'].get('relationships', {}).get('products', {}).get('data', [])
    assert len(products) > 0, "По запросу «ревизор» в результатах поиска продуктов не найдено"

def test_empty_search_phrase(api_client: ApiReadCity):
    try:
        response = api_client.search_product(phrase="")
        assert False, "Ожидалась ошибка HTTP, но запрос выполнен успешно"
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 400, f"Ожидаемый код статус 400, но получили {e.response.status_code}"

        json_response = e.response.json()
        assert "errors" in json_response, "Ожидалось 'errors' в ответе"
        
        error = json_response["errors"][0]
        assert error["code"] == "c1051bb4-d103-4f74-8988-acbcafc7fdc3", "Неожидаемый код ошибки"
        assert error["status"] == "400", "Неожидаемый статус в ответе"
        assert error["title"] == "Phrase обязательное поле", "Неожидаемый ошибка в названии"
        assert error["source"]["pointer"] == "GetSearchProductParams.Phrase", "Неожидаемый указатель источника ошибки"

def test_search_invalid_phrase(api_client: ApiReadCity):
    try:
        response = api_client.search_product(phrase="@$@$@$")
        assert False, "Ожидалась ошибка HTTP, но запрос выполнен успешно"
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 422
        response_data = e.response.json()
        assert "errors" in response_data
        assert len(response_data["errors"]) > 0
        
        error = response_data["errors"][0]
        assert error["code"] == "e91ae96b-2801-46ea-9fd2-416566122f11"
        assert error["status"] == "422"
        assert error["title"] == "Недопустимая поисковая фраза"

def test_add_bookmark(api_client: ApiReadCity):
    book_id = 3026125
    response = api_client.add_bookmark(book_id)

    assert response.status_code in [200, 201], f"Ожидаемый статус код 200 или 201, но получили {response.status_code}"

    assert response.text == "", "Ожидаемое пустое тело ответа"

def test_remove_bookmark(api_client: ApiReadCity):
    book_id = 3026125
    response = api_client.remove_bookmark(book_id)

    assert response.status_code in [200, 204], f"Ожидаемый статус код 200 или 204, но получили {response.status_code}"

    assert response.text == "", "Ожидаемое пустое тело ответа"

def test_update_personal_data(api_client: ApiReadCity):
    personal_data = {
        "lastName": "Sadovina",
        "firstName": "Дарья",
        "middleName": "Александровна",
        "birthday": "1995-09-10",
        "phone": "79877249612",
        "email": "din.tan12@gmail.com",
        "phoneCountry": ""
    }
    
    response = api_client.update_personal_data(personal_data)
    json_response = response.json()

    assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"

    assert json_response["data"] == {
        "birthday": "1995-09-10",
        "email": "din.tan12@gmail.com",
        "firstName": "Дарья",
        "lastName": "Sadovina",
        "middleName": "Александровна",
        "phone": "79877249612"
    }, "Персональные данные в ответе не соответствуют ожидаемым данным"
