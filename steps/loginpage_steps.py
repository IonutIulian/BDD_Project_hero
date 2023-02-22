from behave import *


@when ("Login Page: Enter tomsmith in the username text box")
def step_impl(context):
    context.login_page_object.username()

@when ("Login Page: Enter SuperSecretPassword! in the password text box")
def step_impl(context):
    context.login_page_object.password()

@when ("Login Page: Click on the login button")
def step_impl(context):
    context.login_page_object.press_login()

@then ("I am on the Secure page")
def step_impl(context):
    context.login_page_object.correct_page_checking()


