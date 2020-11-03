@login
Feature: Login
  Scenario: Login to cwb with valid credentials
    Given  user is on login page
    When user enters "email" as "laura+032919+A@jemstep.com" and "password" as "Test1234"
    And user clicks on "login"
    Then user sees page title as "Citi Wealth Builder - Goals"

  Scenario: Login to cwb with invalid credentials
    Given  user is on login page
    When user enters "email" as "laura+032919+A@jemstep.com" and "password" as "Test12345"
    And user clicks on "login"
    Then user sees error message as "Invalid email address or password"