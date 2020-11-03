@signup
Feature: Login to citiwealthbuilder and fill RTQs

  Scenario Outline: Signup into Blue Application
    Given user is on "signup" page
    When user enters <firstName>
    And user enters <LastName>
    And user enters <emailAddress>
    And user enters <password>
    And enters <accessCode>
    Then user clicks on "Signup" button
    And user waits for page load
    Then user verifies "Citi Wealth Builder - Investor Profile" title is displayed

    Examples:
      |firstName|LastName|emailAddress|password|accessCode|
      |pytest|automation |pytest+automation@jemstepqa.com|Welcome1@@|jemstep365|

 Scenario: Signup into Blue Application - Negative
    Given user is on "signup" page
    When  user clicks on "Signup" button
    Then user sees error message as "A first name is required" for "first name" field
    And user sees error message as "A last name is required" for "last name" field
    And user sees error message as "An email address is required" for "email address" field
    And user sees error message as "Access code is required and cannot be empty" for "access code" field
    #And user sees error message as "Must be at least 10 characters long Must contain at least one lowercase and uppercase character Must contain at least one number" for "password" field
    When  user clicks on "Signup" button
    Then user verifies "Citi Wealth Builder - Investor Profile" title is not displayed


