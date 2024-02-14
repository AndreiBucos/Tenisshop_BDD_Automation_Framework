from behave import *

@given ('register: I am a user on the register page')

def step_impl(context):
    context.register_page.navigate_to_register_page()

@when('register: I fill in an user "{user}"')
def step_impl(context,user):
    context.register_page.insert_email(user)

@when('register: I fill in a passwords "{passwords}"')
def step_impl(context,passwords):
    context.register_page.insert_password(passwords)

@when('register: I click on accept terms')
def step_impl(context):
    context.register_page.click_accept_terms()

@when('register: I click the register_button')
def step_impl(context):
    context.register_page.click_register_button()

@Then('register: I verify the already created account error message "{expected_message}"')
def step_impl(context, expected_message):
    context.register_page.created_account_error(expected_message)





