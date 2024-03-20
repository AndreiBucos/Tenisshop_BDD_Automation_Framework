import time
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import Base_Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ForgotPasswordPage(Base_Page):

    EMAIL_INPUT = (By.XPATH, '//input[@class="input-s  " ]')
    SEND_RESET_BUTTON = (By.ID,"_doRecover")
    EMAIL_ERROR_MESSAGE = (By.XPATH, '(//div[@id="email_phone-error"])')
    NOTIFICATION_MESSAGE = (By.XPATH, '//span[@class="hint-order"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="register-page"]/div/div[1]/div/div[3]/form/a[2]')
    FRAME = (By.XPATH, '//iframe[@class="fancybox-iframe"]')


    def navigate_to_forgot_password_page(self):
        self.driver.get('https://tenisshop.ro/recuperare-parola?email=')

    def set_email(self, email):
        iframe=self.driver.find_element(*self.FRAME)
        self.driver.switch_to.frame(iframe)
        if email != "N/A":
            self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)


    def verify_email_error_message(self, expected_message):
        self.check_error_message(expected_message,self.EMAIL_ERROR_MESSAGE)

    def verify_notification_message(self, expected_message):
        self.check_error_message(expected_message, self.NOTIFICATION_MESSAGE)

    def clean_email_text_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def click_new_pass_button(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.SEND_RESET_BUTTON))
        button = self.driver.find_element(*self.SEND_RESET_BUTTON)
        print(f"Am gasit butonul = {button}")
        button.click()

    def click_forgot_pass_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
