from behave import *


@when ("Secure Page: Check if the  verification message is displayed")
def step_impl(context):
    context.secure_page_object.secure_message()

@when ("Secure Page: Click on the logout button")
def step_impl(context):
    context.secure_page_object.press_logout()

@then ("Check if you are on the login page and if the logout message is displayed")
def step_impl(context):
    context.secure_page_object.logout_message_loginpage()
