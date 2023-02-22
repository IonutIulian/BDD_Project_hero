from behave import *


@given("Home page: I am on the herokuapp homepage")
def step_impl(context):
    context.home_page_object.navigate_to_homepage()

@when  ("Home page: I click on Form Authentification")
def step_impl(context):
    context.home_page_object.click_form_auth()

@then ("I am on the Login page")
def step_impl(context):
    context.home_page_object.correct_page_checking()
