from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_Page


class LoginPage(Base_Page):
    EMAIL_INPUT = (By.XPATH, '//input[@type="email"]') #_loginEmail
    PASSWORD_INPUT = (By.XPATH, '//div[@class="old-client-section col-sm-5 pull-right"]//input[@type="password"]')
    LOGIN_BUTTON = (By.ID, 'doLogin')
    LOGIN_ERROR_MESSAGE = (By.XPATH,'//div[@class="errorMsg"]')


    def navigate_to_login_page(self):
        self.driver.get('https://tenisshop.ro/inregistrare/')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def check_login_error_message(self, expected_message):
        self.check_error_message(expected_message,*self.LOGIN_ERROR_MESSAGE)

    def clean_email_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def clean_password_field(self):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()

    def verify_login_error_message(self, expected_message):
        self.check_error_message(expected_message,*self.LOGIN_ERROR_MESSAGE)

