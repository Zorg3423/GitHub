import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPagelocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(
            *ProductPagelocators.ADD_BASKET)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_basket_button(self):
        assert self.is_element_present(
            *ProductPagelocators.ADD_BASKET), "No basket button"

    def should_be_success_message(self):
        product_name = self.browser.find_element(
            *ProductPagelocators.PRODUCT_NAME)
        SUCCESS_MESSAGE = self.browser.find_element(
            *ProductPagelocators.SUCCESS_MESSAGE)
        assert product_name.text == SUCCESS_MESSAGE.text, "Incorrect product in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPagelocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPagelocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
