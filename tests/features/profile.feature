@profile
Feature: Login to CWB and fill profile questionnaire
  Scenario: Fill Profile questionnaire
    Given  user is on login page
    When user enters "email" as "pytest+automation15@jemstepqa.com" and "password" as "Welcome1@@"
    And user clicks on "login"
    Then user sees page title as "Citi Wealth Builder - Investor Profile"
    When user clicks on "Begin"
    Then user enters "DOB" as "01011995"
    And user clicks on "Next question"
    Then user enters "Gross Annual Salary" as "100000"
    And user clicks on "Next question"
    When user selects Investment experience as "Yes"
    Then user sees page title as "Citi Wealth Builder - Goals"

    #pytest+automation12@jemstepqa.com
      #pytest+automation13@jemstepqa.com
   #pytest+automation14@jemstepqa.com

