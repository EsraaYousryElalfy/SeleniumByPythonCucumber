Feature: Search Functionality
# Scenario 1 : valid input
  Scenario Outline: Search for valid product
    Given I got navigated to home page
    When  I enter valid product "<PRODUCTNAME>" into search field
    And   I click on search button
    Then  Valid products should get displayed in search results
    Examples:
      | PRODUCTNAME |
      | HP          |

# Scenario 2 : invalid input
  Scenario Outline: Search for invalid product
    Given I got navigated to home page
    When  I enter invalid product "<PRODUCTNAME>" into search field
    And   I click on search button
    Then  Proper message "<MESSAGE>" should get displayed in search results
    Examples:
      | PRODUCTNAME | MESSAGE                                               |
      | InvalidItem | There is no product that matches the search criteria. |

# Scenario 3 : non input
  Scenario Outline: Search without entering any product
    Given I got navigated to home page
    When  I do not enter anything into search box field
    And   I click on search button
    Then  Proper message "<MESSAGE>" should get displayed in search results
    Examples:
      | MESSAGE                                               |
      | There is no product that matches the search criteria. |