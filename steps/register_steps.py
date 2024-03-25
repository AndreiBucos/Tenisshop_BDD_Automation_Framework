from behave import *

@given ('register: I am a user on the register page')
def step_impl(context):
    context.register_page.navigate_to_register_page()

@when('I expand the register form')
def step_impl(context):
    context.register_page.click_register_button()

@when('register: I fill in a user email "{user}"')
def step_impl(context,user):
    context.register_page.insert_email(user)

@when('register: I fill in an existing user email "{email}"')
def step_impl(context,email):
    context.register_page.insert_existing_email(email)

@when('register: I fill in a user last name "{lastname}"')
def step_impl(context,lastname):
    context.register_page.insert_lastname(lastname)

@when('register: I fill in a user first name "{firstname}"')
def step_impl(context,firstname):
    context.register_page.insert_firstname(firstname)

@when('register: I fill in a user password "{password}"')
def step_impl(context,password):
    context.register_page.insert_password(password)

@when('register: I fill in a confirm user password "{password}"')
def step_impl(context,password):
    context.register_page.insert_confirmation_password(password)

@when('register: I click on accept terms')
def step_impl(context):
    context.register_page.click_accept_terms()

@when('register: I click the register button')
def step_impl(context):
    context.register_page.click_register_button()

@then('register: I verify the already created account error message "{expected_message}"')
def step_impl(context, expected_message):
    context.register_page.created_account_error(expected_message)







