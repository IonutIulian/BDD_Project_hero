
from selenium.webdriver.common.by import By
from browser import Browser

class Home_page(Browser):

    Form_auth = (By.XPATH,"//a[@href='/login']")


    def navigate_to_homepage(self):
        self.chrome.get("https://the-internet.herokuapp.com/")

    def click_form_auth(self):
        self.chrome.find_element(*self.Form_auth).click()

    def correct_page_checking(self):
        correct_url =self.chrome.current_url
        assert correct_url == "https://the-internet.herokuapp.com/login","Error we are on the wrong page."



