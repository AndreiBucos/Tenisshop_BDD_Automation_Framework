from behave import *

@given('I am on home page')
def step_impl(context):
    context.browser.get("https://tenisshop.ro/")

@when ('I click on the search input box')
def step_impl(context):
    context.searched_products_page.search_after()

@then ('I search afer query')
def step_impl(context):
    context.searched_products_page.search_after

@then ('I click search button')
def step_impl(context):
    context.searched_products_page.click_search_button()


@then('products: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.searched_products_page.verify_results_contain_text(query)

@when('I sort products by price from low to high')
def step_impl(context):
    product_page = ProductPage(context.driver)
    product_page.sort_products_by_price_low_to_high()

@then('the products are displayed in ascending order of price')
def step_impl(context):
    product_page = ProductPage(context.driver)
    assert product_page.verify_products_sorted_by_price_low_to_high()