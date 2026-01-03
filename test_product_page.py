import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
links = ["offer0",
         "offer1",
         "offer2",
         "offer3",
         "offer4",
         "offer5",
         "offer6",
         pytest.param("offer7", marks=pytest.mark.xfail),
         "offer8",
         "offer9"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_basket_button()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_empty_basket_text()
