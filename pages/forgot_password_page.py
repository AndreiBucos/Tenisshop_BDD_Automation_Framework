from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import Base_Page


class ForgotPasswordPage(Base_Page):

    EMAIL_INPUT = (By.XPATH, '//input[@class="input-s  " ]')
    SEND_RESET_BUTTON = (By.LINK_TEXT, 'Trimite')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '(//div[@id="email_phone-error"])')
    NOTIFICATION_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="register-page"]/div/div[1]/div/div[3]/form/a[2]')
    FRAME = (By.XPATH, '//iframe[@class="fancybox-iframe"]')



    def navigate_to_forgot_password_page(self):
        self.driver.get('https://tenisshop.ro/recuperare-parola?email=')

    def set_email(self, email):
        iframe=self.driver.find_element(*self.FRAME)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)




    def verify_email_error_message(self, expected_message):
        sleep(3)
        try:
            actual_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def verify_notification_message(self, expected_message):
        #sleep(5)
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def clean_email_text_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    #def click_new_pass_button(self):
        #self.driver.find_element(*self.SEND_RESET_BUTTON).click()

    def click_new_pass_button(self):
        sleep(10)
        self.wait_and_click_elem_by_executor(*self.SEND_RESET_BUTTON)

        #iframe = self.driver.find_element(*self.FRAME)
        #self.driver.switch_to.frame(iframe)
        #button = self.driver.find_element(*self.SEND_RESET_BUTTON)
        #print(f"Am gasit butonul = {button}")
        #button.click()

    def click_forgot_pass_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
