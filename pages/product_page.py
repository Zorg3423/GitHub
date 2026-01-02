import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_BASKET = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_NAME_IN_BASKET = (By.XPATH, "(//div/strong)[3]")

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*self.ADD_BASKET)
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
        assert self.is_element_present(*self.ADD_BASKET), "No basket button"

    def should_be_correct_product_add_to_basket(self):
        product_name = self.browser.find_element(*self.PRODUCT_NAME)
        product_name_in_basket = self.browser.find_element(
            *self.PRODUCT_NAME_IN_BASKET)
        assert product_name.text == product_name_in_basket.text, "Incorrect product in backet"
