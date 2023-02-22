
from selenium.webdriver.common.by import By

from browser import Browser


class Secure_page(Browser):
    Logout_Button = (By.XPATH,"//div[@id='content']//a")
    Verification_mess = (By.ID, 'flash')

    def secure_message(self):
        secure_mess = self.chrome.find_element(*self.Verification_mess).text
        self.assertTrue(secure_mess.is_displayed(),"Error, no message!")
        print(secure_mess)

    def press_logout(self):
        self.chrome.find_element(*self.Logout_Button).click()

    def logout_message_loginpage(self):
        login_url = 'https://the-internet.herokuapp.com/login'
        actual_url = self.chrome.current_url
        assert login_url == actual_url,f"The url's don t match expected {login_url}, actual {actual_url}"
        actual_mess = self.chrome.find_element(*self.Verification_mess).text
        self.assertTrue(actual_mess.is_displayed(), "Error, no message!")
        print(actual_mess)




