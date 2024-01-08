Feature: Register Functionality

  Scenario: Register with mandatory fields
    Given I navigated to register page
    When  I enter details into mandatory fields
    And   I click on continue button
    Then  Account should get created

  Scenario: Register with all fields
    Given I navigated to register page
    When  I enter details into all fields
    And   I click on continue button
    Then  Account should get created

  Scenario: Register with a duplicate email
    Given I navigated to register page
    When  I enter details into all fields except email field
    And   I click on continue button
    Then  Proper warning message informing about duplicate account should be displayed

   Scenario: Register without providing any details
    Given I navigated to register page
    When  I do not enter anything into all field
    And   I click on continue button
    Then  Proper warning message for every mandatory field should be displayed