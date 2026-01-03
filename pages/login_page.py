from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_URL in self.url, "Wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_lOGIN), "Email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_lOGIN), "Password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.BUTTON_LOGIN), "Button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_REGESTRATION), "Email regestration is not presented"
        assert LoginPageLocators.is_element_present(
            *LoginPageLocators.PASSWORD_REGESTRATION), "Password regestration is not presented"
        assert LoginPageLocators.is_element_present(
            *LoginPageLocators.CONFIRM_PASSWORD_REGESTRATION), "Confirm password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.BUTTON_REGESTRATION), "Button regestration is not presented"
