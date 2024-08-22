from page.ui_class_search import SearchPage

def test_search(browser):
    auth_page = SearchPage(browser)
    auth_page.go()