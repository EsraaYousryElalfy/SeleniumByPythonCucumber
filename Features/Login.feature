Feature: Login functionality

  Scenario Outline: Login with valid email address and valid password
    Given I navigated to login page
    When  I enter valid email "<EMAIL>" and valid password "<PASSWORD>"
    And   I click on login button
    Then  I should get login
    Examples:
      | EMAIL                 | PASSWORD |
      | esraaelalfy@email.com | 123456   |

  Scenario Outline: Login with invalid email address and valid password
    Given I navigated to login page
    When  I enter invalid email "<EMAIL>" and valid password "<PASSWORD>"
    And   I click on login button
    Then  I should get proper warning message "<MESSAGE>"
    Examples:
      | EMAIL                 | PASSWORD | MESSAGE                                      |
      | esraaelalfy@email.com | 123456   | No match for E-Mail Address and/or Password. |

  Scenario Outline: Login with valid email address and invalid password
    Given I navigated to login page
    When  I enter valid email "<EMAIL>" and invalid password "<PASSWORD>"
    And   I click on login button
    Then  I should get proper warning message "<MESSAGE>"
    Examples:
      | EMAIL                 | PASSWORD | MESSAGE                                      |
      | esraaelalfy@email.com | 123456   | No match for E-Mail Address and/or Password. |

  Scenario Outline: Login with invalid email address and invalid password
    Given I navigated to login page
    When  I enter invalid email "<EMAIL>" and invalid password "<PASSWORD>"
    And   I click on login button
    Then  I should get proper warning message "<MESSAGE>"
    Examples:
      | EMAIL                 | PASSWORD | MESSAGE                                      |
      | esraaelalfy@email.com | 123456   | No match for E-Mail Address and/or Password. |

  Scenario Outline: Login without entering any credentials
    Given I navigated to login page
    When  I click on login button
    Then  I should get proper warning message "<MESSAGE>"
    Examples:
      | MESSAGE                                      |
      | No match for E-Mail Address and/or Password. |