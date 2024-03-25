from time import sleep
from selenium.webdriver.common.by import By
from browser import Browser
from pages.base_page import Base_Page

class Searched_Products_Page(Browser):

    SEARCH_BUTTON = (By.XPATH, '//i[@class="fa fa-search"]')
    RESULTS_TITLE = (By.CSS_SELECTOR, '.search-results-title')
    INPUT_BOX = (By.ID,'_autocompleteSearchMainHeader')


    def navigate_to_home_page(self):
        sleep(3)
        self.driver.get('https://tenisshop.ro/')

    def click_search_input_box(self):
        self.driver.find_element(*self.INPUT_BOX).click()


    def search_after(self,query):
        self.driver.find_element(*self.INPUT_BOX).send_keys(query)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        sleep(2)

    def verify_results_contain_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for element in title_list:
            title = element.text.lower()
            assert text in title, f'Result does not contain search query'





