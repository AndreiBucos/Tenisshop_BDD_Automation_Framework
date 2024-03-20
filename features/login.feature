Feature: Check the Login functionality

  Background:
    Given login: I am a user on the login page

  @login_test
  Scenario: Enter wrong credentials and check the error
    When base: I accept the cookies popup
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then forgot_pass: I verify that I receive the correct error message "Hm... Utilizatorul sau parola? Ceva nu corespunde :("

  @empty_login_test
  Scenario: Leave empty login fields
    When base: I accept the cookies popup
    When login: I make sure that email input is cleared
    When login: I make sure that password input is cleared
    When login: I click the login button
    Then login: I verify the empty email error message "Acesta este un camp obligatoriu."
    Then login: I verify the empty password error message "Acesta este un camp obligatoriu."