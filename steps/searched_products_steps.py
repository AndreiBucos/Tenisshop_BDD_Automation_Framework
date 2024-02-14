from behave import *


@then('products: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.searched_products_page.verify_results_contain_text(query)
