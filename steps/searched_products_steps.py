from behave import *

@given('I am on home page')
def step_impl(context):
    context.browser.get("https://tenisshop.ro/")

@when ('search: I click on the search input box')
def step_impl(context):
    context.searched_products_page.click_search_input_box()

@then ('search: I search after "{query}"')
def step_impl(context,query):
    context.searched_products_page.search_after(query)

@then ('search: I click search button')
def step_impl(context):
    context.searched_products_page.click_search_button()


@then('search: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.searched_products_page.verify_results_contain_text(query)
