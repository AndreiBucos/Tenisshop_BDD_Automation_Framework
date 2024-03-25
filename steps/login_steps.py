from time import sleep

from behave import *

@given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('login: I fill in an email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I fill in a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@when('login: I make sure that email input is cleared')
def step_impl(context):
    context.login_page.clean_email_field()

@when('login: I make sure that password input is cleared')
def step_impl(context):
    context.login_page.clean_password_field()

@then('login: I verify that I receive the correct email and password error message "{error_message}"')
def step_impl(context,error_message):
    context.login_page.verify_login_error_message(error_message)




