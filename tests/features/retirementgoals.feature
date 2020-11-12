Feature:  Investor Login to CWB and completes fillings RTQs

  @GoalScenario
  Scenario Outline: An Investor Login to Citi wealth builder and completes Retriement Goal Creation
    Given an Investor visits the Login page
    When they log in with "goalquestionaireCredentials"
    Then they are taken to the "Citi Wealth Builder - Goals" page
    When they click "create a new goal"
    Then they click "Retirement Fund"
    And they click Goal "Begin"
    Then they enter their goal name as "My Retirment Goal"
    When they enter their desired monthly spend in Retirement as "500,000"
    And they click Goal "Next"
    Then they are prompted with the below message for Desired monthly spent
      | DesiredMonthlySpendErrorMessage | Enter a valid monthly spend between $500 to $100,000. |
    When they enter their desired monthly spend in Retirement as "50,000"
    And they click Goal "Next"
    Then they enter their Retirement age as "70"
    And they click Goal "Next"
    Then they select their secure future income as <FutureIncomeOption>
    Then they select their monthly savings as <MonthlySavingsOption>
    Then they select their risk comfort level as <RiskComfortLevel>
    Then they select their investment fell reaction as <InvestmentFallReaction>
    Then they select their primary concern to goal as <GoalConcern>
    Then they enter their monthly savings as "$3,000"
    And they click Goal "Next"
    And they enter their retirement goal savings as "5,000,000"
    And they click Goal "Next"
    And they click "SEE MY ESTIMATED RETIREMENT SPEND"
    And they click "Next: RECOMMENDED ALLOCATION"
    Then user verifies the target model as <riskScoreExpectedModel>
    And they click "Next: Open accounts"
    Then they are taken to the "Map Accounts" page
    Examples:
      | FutureIncomeOption | MonthlySavingsOption | RiskComfortLevel              | InvestmentFallReaction | GoalConcern                                          | riskScoreExpectedModel                                        |
      | Secure             | 1 to 3 months        | I'm willing to take some risk | I'd wait and see       | Most concerned about not reaching my retirement goal | Moderate Growth portfolio offered through Citi Wealth Builder |