from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

# Для запуска тестов
# pytest -v -s --tb=line --language=en test_main_page.py
# pytest -v -s -m "login_guest" --tb=line --language=en test_main_page.py


link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # pytest -v -s -m login_guest --tb=line --language=en test_main_page.py
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_login_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.open_cart()
    page.should_be_no_empty_cart()
    page.should_be_empty_cart()
