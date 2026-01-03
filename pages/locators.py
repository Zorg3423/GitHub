from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    ### ----- Кнопа логина ----- ###
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ### ----- Форма ссылки ----- ###
    LOGIN_URL = "/accounts/login/"
    ### ----- Форма авторизации ----- ###
    EMAIL_lOGIN = (By.XPATH, "//input[@name='login-username']")
    PASSWORD_lOGIN = (By.XPATH, "//input[@name='login-password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@name='login_submit']")
    ### ----- Форма регистрации ----- ###
    EMAIL_REGESTRATION = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_REGESTRATION = (By.XPATH,
                             "//input[@name='registration-password1']")
    CONFIRM_PASSWORD_REGESTRATION = (By.XPATH,
                                     "//input[@name='registration-password2']")
    BUTTON_REGESTRATION = (By.XPATH,
                           "//button[@name='registration_submit']")


class ProductPagelocators:
    ADD_BASKET = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    SUCCESS_MESSAGE = (By.XPATH, "(//div/strong)[3]")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
