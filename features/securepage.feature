Feature: Test the secure area


  Background:
    Given Home page: I am on the herokuapp homepage


  Scenario: Check the secure page
    When  Home page: I click on Form Authentification
    When  Login Page: Enter tomsmith in the username text box
    When  Login Page: Enter SuperSecretPassword! in the password text box
    When  Login Page: Click on the login button
    When  Secure Page: Check if the  verification message is displayed
    When  Secure Page: Click on the logout button
    Then  Check if you are on the login page and if the logout message is displayed