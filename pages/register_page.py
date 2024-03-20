from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from pages.base_page import Base_Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Register_Page(Base_Page):
    EMAIL_INPUT = (By.ID, "__emailRegister")
    LASTNAME_INPUT = (By.ID, "__lastnameRegister")
    FIRSTNAME_INPUT = (By.ID, "__firstnameRegister")
    PASSWORD_INPUT = (By.ID, "__passwordRegister")
    CONFIRM_PASSWORD_INPUT = (By.ID, "__confirmPasswordRegister")
    TERMS_CHECKBOX = (By.XPATH, '//input[@name="agreePersonalInformation"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="doRegister"]')
    CREATED_ACCOUNT_ERROR_MESSAGE= (By.CSS_SELECTOR, "div[class='success-msg'] h4")

    def navigate_to_register_page(self):
        self.driver.get("https://tenisshop.ro/inregistrare")
        sleep(10)

    def insert_email(self, user):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(user)


    def insert_lastname(self, user):
       self.driver.find_element(*self.LASTNAME_INPUT).send_keys(user)

    def insert_firstname(self, user):
       self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(user)

    def insert_password(self,passwords):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(passwords)

    def insert_confirmation_password(self, passwords):
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(passwords)

    def click_accept_terms(self):
        self.driver.find_element(*self.TERMS_CHECKBOX).click()

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def created_account_error(self, expected_message):
        sleep(3)
        try:
            actual_message = self.driver.find_element(*self.CREATED_ACCOUNT_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect'
