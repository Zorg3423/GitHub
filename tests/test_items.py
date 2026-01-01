import time


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Для визуальной проверки языка (по заданию)
    time.sleep(30)

    add_to_basket_button = browser.find_element(
        "css selector", "button.btn-add-to-basket"
    )

    assert add_to_basket_button is not None, "Add to basket button is not found"
