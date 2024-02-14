from browser import Browser
from pages.base_page import Base_Page
from pages.register_page import Register_Page
from pages.forgot_password_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.searched_products_page import Searched_Products_Page


def before_all(context):
    context.browser = Browser()
    context.base_page = Base_Page()
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.home_page = HomePage()
    context.searched_products_page = Searched_Products_Page()
    context.register_page = Register_Page()


def after_all(context):
    context.browser.close()
