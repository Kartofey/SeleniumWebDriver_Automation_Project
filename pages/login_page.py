from .base_page import BasePage
from .locators import LoginPageLocators

# Класс методов для страниц авторизации и регистрации
class LoginPage(BasePage):

# Метод для регистрации нового пользователя
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2)
        password_input2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

# Проверка правильности url, наличия форм авторизации и регистрации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

# Проверка правильности url
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It's not login page's url"

# Проверка наличия формы авторизации
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

# Проверка наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

# Проверка наличия сообщения о подтверждении успешности регистрации
    def should_be_success_registration_message(self):
        assert self.is_element_present(*LoginPageLocators.WELCOME_MESSAGE), "Success registration message is not presented"
