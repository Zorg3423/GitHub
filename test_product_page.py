import pytest
import time
from .pages.product_page import ProductPage

links = ["offer0",
         "offer1",
         "offer2",
         "offer3",
         "offer4",
         "offer5",
         "offer6",
         pytest.param("offer7", marks=pytest.mark.xfail),
         "offer9",
         "offer0"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_add_to_basket()
