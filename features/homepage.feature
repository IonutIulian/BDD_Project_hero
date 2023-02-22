Feature: Test the herokuapp homepage

  Background:
    Given Home page: I am on the herokuapp homepage

  Scenario: Check that the user can acces the login page
    When  Home page: I click on Form Authentification
    Then  I am on the Login page




