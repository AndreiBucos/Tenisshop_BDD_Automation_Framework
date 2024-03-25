from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('login: I click on the forgot password link')
def step_impl(context):
    context.forgot_password_page.click_forgot_pass_link()

@when('forgot_pass: I fill in my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)

@when('forgot_pass: I click on the send button')
def step_impl(context):
    context.forgot_password_page.click_send_button()

@then('forgot_pass: I verify that I receive the correct error message "{error_message}"')
def step_impl(context, error_message):
    context.forgot_password_page.verify_email_error_message(error_message)

