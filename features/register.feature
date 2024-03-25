Feature: Check the register functionality

  Background:
    Given register: I am a user on the register page

  @register_successful
Scenario: Enter correct credentials and create a new account
    When base: I accept the cookies popup
    When I expand the register form
    When register: I fill in a user email "anndreiy_22m@yahoo.com"
    When register: I fill in a user last name "Bucos"
    When register: I fill in a user first name "Andrei"
    When register: I fill in a user password "Caisa100"
    When register: I fill in a confirm user password "Caisa100"
    When register: I click on accept terms
    When register: I click the register button
    Then home: Check the url to be "https://tenisshop.ro/contul-meu?registration=success"

  @client_already_registered
  Scenario: Try to register with the credentials of an already created account
    When base: I accept the cookies popup
    When I expand the register form
    When register: I fill in an existing user email "andrei.bucos@yahoo.com"
    When register: I fill in a user last name "Test"
    When register: I fill in a user first name "Test"
    When register: I fill in a user password "Test1234"
    When register: I fill in a confirm user password "Test1234"
    When register: I click on accept terms
    When register: I click the register button
    Then register: I verify the already created account error message "Adresa de email exista in baza de date. Va rugam sa va logati."

