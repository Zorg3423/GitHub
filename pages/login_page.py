from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_URL = "/accounts/login/"
    ### ----- Форма авторизации ----- ###
    EMAIL_lOGIN = (By.XPATH, "//input[@name='login-username']")
    PASSWORD_lOGIN = (By.XPATH, "//input[@name='login-password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@name='login_submit']")
    ### ----- Форма регистрации ----- ###
    EMAIL_REGESTRATION = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_REGESTRATION = (
        By.XPATH, "//input[@name='registration-password1']")
    CONFIRM_PASSWORD_REGESTRATION = (
        By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REGESTRATION = (By.XPATH, "//button[@name='registration_submit']")

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.LOGIN_URL in self.url, "Wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *self.EMAIL_lOGIN), "Email is not presented"
        assert self.is_element_present(
            *self.PASSWORD_lOGIN), "Password is not presented"
        assert self.is_element_present(
            *self.BUTTON_LOGIN), "Button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *self.EMAIL_REGESTRATION), "Email regestration is not presented"
        assert self.is_element_present(
            *self.PASSWORD_REGESTRATION), "Password regestration is not presented"
        assert self.is_element_present(
            *self.CONFIRM_PASSWORD_REGESTRATION), "Confirm password is not presented"
        assert self.is_element_present(
            *self.BUTTON_REGESTRATION), "Button regestration is not presented"
