from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        """Метод проверяет наличие всех форм на странице регистрации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_password_regist1_form()
        self.should_be_password_regist2_form()
        self.should_be_password_login_form()

    def should_be_login_url(self):
        """Метод проверяет ссылку авторизации"""
        assert 'login' in self.browser.current_url, "Incorrect login url"

    def should_be_login_form(self):
        """Метод проверяет наличие формы для ввода логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        """Метод проверяет наличие формы для ввода email в форме регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Registration form is not presented"

    def should_be_password_login_form(self):
        """Метод проверяет наличие формы для ввода пароля при авторизации"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Password for login is not presented"

    def should_be_password_regist1_form(self):
        """Метод проверяет наличие формы для ввода пароля при регистрации. Форма1"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1), \
            "Password for registretion is not presented"

    def should_be_password_regist2_form(self):
        """Метод проверяет наличие формы для ввода пароля при регистрации. Форма2"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2), \
            "Password for registretion is not presented"

    def register_new_user(self, email, password):
        """Метод регистрирует нового пользователя"""
        self.should_be_login_page()
        form_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        form_email.send_keys(email)
        form_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        form_password1.send_keys(password)
        form_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        form_password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
