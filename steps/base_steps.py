from behave import *


@when('base: I accept the cookies popup')
def step_impl(context):
    context.base_page.click_accept_cookies_btn()
    #context.base_page.click_close_popup_btn()

