from browser import Browser
from pages.homepage import Home_page
from pages.loginpage import Login_page
from pages.securepage import Secure_page


def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.login_page_object = Login_page()
    context.secure_page_object = Secure_page()

def after_all(context):
    context.browser.close()
