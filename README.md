# FP_ui_api_pytest

## Дипломная работа по курсу - Автоматизация тестирования на Python

### Уточнения по работе
Для написания UI-тестов выбрана только одна функция — проверка поля "Поиск". Это обусловлено тем, что для остальных выбранных проверок на сайте "Читай-город" авторизация возможна только по номеру телефона с использованием СМС-кода.

API-тесты выполнены методами GET, POST, DELETE и PATCH. Данные для тестирования были взяты из функционального тестирования API (backend). Для метода GET написаны как позитивный, так и негативный сценарии.

Также токен сайта обновляется часто, поэтому в фикстуре нужно менять его.

### Шаги:
1. Склонировать проект 'git clone https://github.com/Mimzaaa/FP_ui_api_pytest.git'
2. Установить зависимости 
3. Прописать ui-тесты
4. Прописать api-тесты
3. Запустить тесты 'pytest --alluredir=./allure-results'
4. Сгенерировать отчет 'allure generate allure-results -o allure-report'
5. Открыть отчет 'allure serve allure-results'

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД (!)

### Полезные ссылки:
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки: (!)
- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure-pytest
- pip3 install requests