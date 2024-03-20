Feature: Tennis-Zone search feature

    Background:
      Given home: I am on home page

    @search
    Scenario Outline: Test search functionality
      When base: I accept the cookies popup
      When I click on the search input box
      Then home: I search after "<query>"
      Then home: I click search button
      Then products: I verify that results contain search query "<query>"

    Examples:
      | query    |
      | rachete  |
      | mingi    |
      | tricou   |

  #Scenario: Sort products by price from low to high
   # Given I am on the homepage of the website
    #When I sort products by price from low to high
    #Then The products are displayed in ascending order of price



#      De adaugat scenarii in care se face sortare: crescatoare / descrescatoare si verifici ca rezultatele sunt in ordine
#      De adaugat scenariu in care se face sortare dupa discount si verifici ca elementele sunt sortate corespunzator


