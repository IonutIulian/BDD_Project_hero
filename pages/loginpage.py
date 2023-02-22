from selenium.webdriver.common.by import By

from browser import Browser


class Login_page(Browser):
    Username = (By.ID,"username")
    Password = (By.ID,"password")
    Login_Button = (By.XPATH,"//form[@id='login']/button")

    def username(self):
        self.chrome.find_element(*self.Username).send_keys("tomsmith")

    def password(self):
        self.chrome.find_element(*self.Password).send_keys("SuperSecretPassword!")

    def press_login(self):
        self.chrome.find_element(*self.Login_Button).click()

    def correct_page_checking(self):
        correct_url = self.chrome.current_url
        assert correct_url == "https://the-internet.herokuapp.com/secure", "Error we are on the wrong page."