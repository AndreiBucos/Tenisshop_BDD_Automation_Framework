Feature: Check the register functionality

  Background:
    Given register: I am a user on the register page

  @register_successfull
Scenario: Enter correct credentials and create a new account
    Then : I click the register_button
    When register: I fill in an user email "anndreiy_22m@yahoo.com"
    When register: I fill in a user last name "Bucos"
    When register: I fill in a user first name "Andrei"
    When register: I fill in a user password "Caisa100"
    When register: I fill in a confirm user password "Caisa100"
    When register: I click on accept terms
    When register: I click the register_button
    Then home: Check the url to be "https://tenisshop.ro/"

  @client_already_registered
  Scenario: Try to register with the credentials of an already created account
    When register: I fill in an user "andrei.bucos@yahoo.com"
    When register: I fill in a user last name "Test"
    When register: I fill in a user first name "Test"
    When register: I fill in a passwords "Test1234"
    When register: I fill in a confirm user password "Test1234"
    When register: I click on accept terms
    When register: I click the register_button
    Then forgot_pass: I verify that I receive the correct error message "Datele dvs. de acces nu au putut fi atribuite unui utilizator"

