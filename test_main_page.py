import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLogimFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products()
        basket_page.should_be_empty_basket_text()
