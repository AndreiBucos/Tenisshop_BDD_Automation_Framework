from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class Base_Page(Browser):

    ACCEPT_COOKIES_BTN = (By.ID, "__gomagCookiePolicy")
    #CLOSE_POPUP_BTN = (By.XPATH, '//div[@class="close-button"]')

    def click_accept_cookies_btn(self):
        self.click_element_by_selector(*self.ACCEPT_COOKIES_BTN)

    #def click_close_popup_btn(self):
        #self.click_if_present_by_selector(*self.CLOSE_POPUP_BTN)

    def click_if_present_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        if len(elem_list) == 1:
            self.wait_scroll_and_click_elem_by_selector(by, selector)
    def click_element_by_selector(self, by, selector):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        elem.click()

    def wait_scroll_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def hover_by_elem(self, elem):
        actions = ActionChains(self.driver).move_to_element(elem)
        actions.perform()
        #sleep(1)


    def wait_and_click_elem_by_executor(self, by, selector):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].click();", elem)