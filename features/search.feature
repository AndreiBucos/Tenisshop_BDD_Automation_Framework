Feature: Tennis-Zone search feature

    Background:
      Given home: I am on home page

    @search
    Scenario Outline: Test search functionality
      When home: I search after "<query>"
      Then home: I click search button
      Then products: I verify that results contain search query "<query>"

    Examples:
      | query    |
      | rachete  |
      | mingi    |
      | tricou   |

      # pas nou: returnare rezultate pentru caturai
  # cautarea unui produs dupa o sortare si verificarea sortarii (pret eg)