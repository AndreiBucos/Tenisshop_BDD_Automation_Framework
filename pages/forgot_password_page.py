from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import Base_Page


class ForgotPasswordPage(Base_Page):

    EMAIL_INPUT = (By.XPATH, '//input[@id="email_phone"]')
    NEW_PASS_BUTTON = (By.XPATH, '//button[@class="action submit primary"]')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '(//div[@id="email_phone-error"])') #inseram un e-mail invalid
    NOTIFICATION_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')  #nu scriem nimic in campul e-mail

    def navigate_to_forgot_password_page(self):
        self.driver.get('https://tenisshop.ro/recuperare-parola?email=')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def verify_email_error_message(self, expected_message):
        sleep(3)
        try:
            actual_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None' #nu s-a afisat elementul

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def verify_notification_message(self, expected_message):
        sleep(5)
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None' #daca nu apare niciun mesaj, nu vrem sa fie afisat elementul respectiv

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def clean_email_text_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def click_new_pass_button(self):
        self.driver.find_element(*self.NEW_PASS_BUTTON).click()


