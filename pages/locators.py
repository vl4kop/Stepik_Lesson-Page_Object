from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_CART = (By.CSS_SELECTOR, 'span.btn-group a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')

    NAME_OF_BOOK_IN_CART = (By.CSS_SELECTOR, 'div.alertinner strong')
    CHECK_NAME_OF_BOOK = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_VALUE = (By.CSS_SELECTOR, 'div.alert-info div.alertinner strong')
    CHECK_BASKET_VALUE = (By.CSS_SELECTOR, 'div.product_main p.price_color')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')


class BasketPageLocators:
    EMPTY_CART = (By.CSS_SELECTOR, '#content_inner > p')
    NOT_EMPTY_CART = (By.CSS_SELECTOR, '#basket_formset')