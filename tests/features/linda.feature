Feature: Create an user account
  (only Keybank and CWB)

  Scenario: An user succesfully ceates an account via SSO or magic link
    Given User is able to access the system via single sign-on (SSO) from their financial organization's website or a magic link and land on the "Profile" page
    When User click "Begin"
    Then User are taken to the first profile question - where the age is greyed out and un-editable
    When User click "Next"
    Then User enter their gross annual income as "$3,000,000"
    And they click "Next"
    Then User are prompted with the GrossAnnual error message
      | GrossAnnualIncomeErrorMessage | Enter a valid annual income between $0 and $2,000,000 |
    When User enter their gross annual income as "$0"
    And they click "Next"
    Then User are prompted with the GrossAnnual error message
      | GrossAnnualIncomeErrorMessage | Enter a valid annual income between $0 and $2,000,000 |
    And they enter their gross annual income as "$1,000,000"
    When User click "Next"
    And they select their investment experience option as "None"
    Then User are asked to learn about ETFs before proceeding
    When User select their investment experience option as "Limited/Moderate/Extensive"
    Then User see "Goals" page

  Scenario: An user succesfully ceates an account via NON - SSO
    Given A user reaches the "User Signup" page
    When User signs up with a new user
      | new user |
    And select the "Sign Up"
    Then User land on the "Profile page"
    When User click "Begin"
    Then User enter their date of birth as "01/01/2020"
    And they click "Next"
    Then User are prompted with the below message
      | DateofBirthErrorMessage | You must be between 18 and 85 years old to open an account. |
    When User enter their date of birth as "01011910"
    And they click "Next"
    Then User are prompted with the below message
      | DateofBirthErrorMessage | You must be between 18 and 85 years old to open an account. |
    When User enter their date of birth as "01011980"
    And they click "Next"
    Then User enter their gross annual income as "$3,000,000"
    And User click "Next"
    Then User are prompted with the GrossAnnual error message
      | GrossAnnualIncomeErrorMessage | Enter a valid annual income between $0 and $2,000,000 |
    When User enter their gross annual income as "$0"
    And they click "Next"
    Then User are prompted with the GrossAnnual error message
      | GrossAnnualIncomeErrorMessage | Enter a valid annual income between $0 and $2,000,000 |
    And User enter their gross annual income as "$1,000,000"
    When User click "Next"
    And they select their investment experience option as "None"
    Then User are asked to learn about ETFs before proceeding
    When User select their investment experience option as "Limited/Moderate/Extensive"
    Then User see "Goals" page

  Scenario: Testing the validations on the Singup
    Given A user reaches the "User Signup" page
    When User select sign up
    Then all fields will display and error message stating that the field is required
    When User fill in first name "1234567890o1234567890t1234567890t1234567890f1234567890f1234567890s1234567890s1234567890e1234567890n1234567890t"
    Then User are prompted with the error message
      | Maximum of 100 characters |
    When User fill in first name "!james*"
    Then User are prompted with the error message
      | Special characters not allowed |
    When User fill in first name "James"
    And they fill in last name "1234567890o1234567890t1234567890t1234567890f1234567890f1234567890s1234567890s1234567890e1234567890n1234567890t"
    Then User are prompted with the error message
      | Maximum of 100 characters |
    When User fill in last name "!Smith*"
    Then User are prompted with the error message
      | Special characters not allowed |
    When User fill in an email address "jamessmith.com"
    Then User are prompted with the error message
      | Email address is not valid |
    When User fill in an email address "jamessmith@com"
    Then User are prompted with the error message
      | Email address is not valid |
    When User fill in email address "jamessmith@gmail.com"
    And they fill in a password "house"
    Then thUserey are prompted with the error message
      | Must be at least 10 characters long
  Must contain at least one lowercase and uppercase character
  Must contain at least one number
  Must contain at least one special character e.g. '! @ # $ % ^ & * _ -'|
    When User fill in a password "House123"
    Then User are prompted with the error message
      | Must be at least 10 characters long
  Must contain at least one special character e.g. '! @ # $ % ^ & * _ -'|
    When User fill in a password "House123!"
    Then User are prompted with the error message
      | Must be at least 10 characters long |
    And they fill in password with "House1234!"
    When User fill in access code "jemstep365"
    And they select sign up
    Then User land on the "Profile" page