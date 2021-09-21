from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Incorrect URL Adress"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form doesn`t exist"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), "Login form doesn`t exist"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        repeat_password_field.send_keys(password)
        registration_btn = self.browser.find_element(*LoginPageLocators.REGISRATION_BUTTON)
        registration_btn.click()
