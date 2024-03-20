from behave import *

@given('I am on the login page')
def step_impl(context):
    context.browser.get("https://tenisshop.ro/inregistrare")

@when('login: I click on the forgot password link')
def step_impl(context):
    context.forgot_password_page.click_forgot_pass_link()


@then('I should be redirected to the forgot password page')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.url_contains("forgot_password"))

@when('forgot_pass: I fill in my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)


@when('forgot_pass: I click on the send button')
def step_impl(context):
    context.forgot_password_page.click_new_pass_button()


@then('I verify that I receive the correct error message {"error_message"}')
def step_impl(context):
    pass

@when('forgot_pass: I make sure that email input is cleared')
def step_impl(context):
    context.forgot_password_page.clean_email_text_field()

