Feature: Check the Login functionality

  Background:
    Given login: I am a user on the login page

  @login_test
  Scenario: Enter wrong credentials and check the error
    When base: I accept the cookies popup
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then login: I verify that I receive the correct email and password error message "Adresa de e-mail / parola introduse sunt incorecte. Te rugam sa incerci din nou."

  @empty_login_test
  Scenario: Leave empty login fields
    When base: I accept the cookies popup
    When login: I make sure that email input is cleared
    When login: I make sure that password input is cleared
    When login: I click the login button
    Then login: I verify that I receive the correct email and password error message "Adresa de e-mail / parola introduse sunt incorecte. Te rugam sa incerci din nou."