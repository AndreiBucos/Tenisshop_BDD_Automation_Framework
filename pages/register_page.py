import random

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from pages.base_page import Base_Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Register_Page(Base_Page):
    EMAIL_INPUT = (By.XPATH, '//label[contains(text(),"Email*")]//following-sibling::input')
    LASTNAME_INPUT = (By.XPATH, '//label[contains(text(),"Nume*")]//parent::div//input[@type="text"]')
    FIRSTNAME_INPUT = (By.XPATH, '//label[contains(text(),"Prenume*")]//parent::div//input[@type="text"]')
    PASSWORD_INPUT = (By.XPATH, '//label[contains(text(),"Parola*")]//parent::div//input[@type="password"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//label[contains(text(),"Confirma parola*")]//following-sibling::input')
    LOGOUT_BUTTON = (By.XPATH,'//a[contains(text(),"Logout")]')
    TERMS_CHECKBOX = (By.XPATH, '//input[@name="agreePersonalInformation"]')
    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Inregistreaza-te")]')
    CREATED_ACCOUNT_ERROR_MESSAGE= (By.XPATH, '//label[contains(text(),"Email*")]//following-sibling::span')

    def navigate_to_register_page(self):
        self.driver.get("https://tenisshop.ro/inregistrare")

    def insert_email(self, email):
        number = random.randint(0,99999999999999999)
        self.wait_element(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(f"{number}{email}")

    def insert_existing_email(self,email):
        self.wait_element(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def insert_lastname(self, user):
        self.wait_element(*self.LASTNAME_INPUT)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(user)

    def insert_firstname(self, user):
        self.wait_element(*self.FIRSTNAME_INPUT)
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(user)

    def insert_password(self,passwords):
        self.wait_element(*self.PASSWORD_INPUT)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(passwords)

    def insert_confirmation_password(self, passwords):
        self.wait_element(*self.CONFIRM_PASSWORD_INPUT)
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(passwords)

    def click_logout_button(self):
        try:
            self.driver.find_element(*self.LOGOUT_BUTTON).click()
        except:
            pass


    def click_accept_terms(self):
        self.driver.find_element(*self.TERMS_CHECKBOX).click()

    def click_register_button(self):
        try:
            self.wait_element(*self.REGISTER_BUTTON)
            self.driver.find_element(*self.REGISTER_BUTTON).click()
        except:
            pass


    def created_account_error(self, expected_message):
        self.check_error_message(expected_message,*self.CREATED_ACCOUNT_ERROR_MESSAGE)


