from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_Page


class LoginPage(Base_Page):
    EMAIL_INPUT = (By.NAME, 'login[credentials]')
    PASSWORD_INPUT = (By.NAME, 'login[password]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="send2"]')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Ai uitat parola")
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//div[@class="message-error error message"]')
    EMPTY_EMAIL_ERROR = (By.XPATH, '//div[@id="credentials-error"]')
    EMPTY_PASS_ERROR = (By.XPATH, '//div[@id="pass-error"]')

    def navigate_to_login_page(self):
        self.driver.get('https://tenisshop.ro/inregistrare/')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def check_login_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"

        #assert actual_message == expected_message, f'Error, the message is incorrect'
        EC.text_to_be_present_in_element((By.XPATH, '//div[@class="message-error error message"]'), expected_message)

    def click_forgot_password_link(self):
        #self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
        link = self.driver.find_element(*self.FORGOT_PASSWORD_LINK)
        self.driver.execute_script("arguments[0].click();", link)

    def clean_email_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def clean_password_field(self):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()

    def empty_email_error_message(self, expected_message):
        sleep(3)
        try:
            actual_message = self.driver.find_element(*self.EMPTY_EMAIL_ERROR).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def empty_password_error_message(self, expected_message):
        sleep(3)
        try:
            actual_message = self.driver.find_element(*self.EMPTY_PASS_ERROR).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect'
