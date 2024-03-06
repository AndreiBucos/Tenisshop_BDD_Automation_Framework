Feature: Check the register functionality

  Background:
    Given register: I am a user on the register page

  @register_successfull
Scenario: Enter correct credentials and create a new account
    When register: I fill in an user "anndreiy_22m@yahoo.com"
    When register: I fill in an user "anndreiy_22m@yahoo.com"
    When register: I fill in a passwords "Caisa100"
    When register: I fill in a passwords "Caisa100"
    When register: I click on accept terms
    When register: I click the register_button
    Then home: Check the url to be "https://tenisshop.ro/"

  @client_already_registered

  Scenario: Try to register with the credentials of an created account
    When register: I fill in an user "andrei.bucos@yahoo.com"
    When register: I fill in a passwords "Test1234"
    When register: I click on accept terms
    When register: I click the register_button
    Then register: I verify the already created account error message "Datele dvs. de acces nu au putut fi atribuite unui utilizator"

