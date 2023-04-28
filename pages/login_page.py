from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It's not login page's url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2)
        password_input2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_success_registration_message(self):
        assert self.is_element_present(*LoginPageLocators.WELCOME_MESSAGE), "Register form is not presented"
