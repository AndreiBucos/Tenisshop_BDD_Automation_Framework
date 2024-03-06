from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Base_Page

class HomePage(Base_Page):
    LOGO_IMG = (By.XPATH, '//*[@id="logo"]/img')
    SEARCH_INPUT = (By.XPATH, '//*[@id="_autocompleteSearchMainHeader"]')
    SEARCH_BTN = (By.XPATH, '//*[@id="_doSearch"]')
    MENU_BTN = (By.XPATH, '//*[@id="main-menu"]/div/ul')

    def navigate_to_home_page(self):
        sleep(5)
        self.driver.get('https://tenisshop.ro/')

    def click_logo_img(self):
        #sleep(1)
        self.driver.find_element(*self.LOGO_IMG).click()

    def search_after(self, query):
        #sleep(1)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(query)

    def click_search_btn(self):
        self.driver.find_element(*self.SEARCH_BTN).click()
        #sleep(1)

    def verify_page_url(self, expected_url):
        #sleep(1)
        actual = self.driver.current_url
        assert actual == expected_url, f'URL este gresit'

    def click_menu_btn(self):
        #sleep(1)
        self.driver.find_element(*self.MENU_BTN).click()

    def hover_over_menu_category(self, category_name):
        #sleep(1)
        elem = self.driver.find_element(By.CLASS_NAME, "main-menu > div > ul > li:nth-child(1) > a > span")
        self.hover_by_elem(elem)

    def hover_over_menu_subcategory(self, subcategory_name):
        #sleep(1)
        elem = self.driver.find_element(By.CLASS_NAME, "main-menu > div > ul > li:nth-child(1)")
        self.hover_by_elem(elem)



