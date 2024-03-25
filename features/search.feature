Feature: Tennis-Zone search feature

    Background:
      Given home: I am on home page

    @search
    Scenario Outline: Test search functionality
      When base: I accept the cookies popup
      When search: I click on the search input box
      Then search: I search after "<query>"
      Then search: I click search button
      Then search: I verify that results contain search query "<query>"

    Examples:
      | query    |
      | rachete  |


