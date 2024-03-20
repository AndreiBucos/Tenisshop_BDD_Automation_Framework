Feature: Check the Forgot password functionality

  Background:
    Given login: I am a user on the login page

  @invalid_email
  Scenario Outline: Check that correct error message is returned when inserting invalid or non-existing email in the reset pass form
    When base: I accept the cookies popup
    When login: I click on the forgot password link
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the send button
    Then forgot_pass: I verify that I receive the correct error message "<expected_error>"

  Examples:
    | email          | expected_error                                          |  |
    | test           | - Adresa de email este invalida.                        |  |
    | my_email@      | - Adresa de email este invalida.                        |  |
    | N/A            | Acesta este un camp obligatoriu.                        |  |
    | test@gmail.com | - Adresa de email nu este inregistrata in baza de date. |  |


