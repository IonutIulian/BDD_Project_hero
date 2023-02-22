Feature: Test The functionality of login page

  Background:
    Given Home page: I am on the herokuapp homepage

  Scenario: Check that the user can login
    When  Home page: I click on Form Authentification
    When  Login Page: Enter tomsmith in the username text box
    When  Login Page: Enter SuperSecretPassword! in the password text box
    When  Login Page: Click on the login button
    Then  I am on the Secure page