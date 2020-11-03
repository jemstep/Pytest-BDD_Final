class locators:
    # LoginPage elements
    email_txtbox_name = "#emailAddress"
    pass_txtbox_name = "#password"
    login_btn_name = "btn-login"

    # Signup Page elements
    firstname_txtbox = "#firstName"
    lastname_txtbox = "#lastName"
    emailAddr_txtbox = "#emailAddress"
    password_txtbox = "#password"
    accessCode_txtbox = "#accessCode"
    signup_btn = "btn-signup"

    # Error validations
    firstname_err = "(//div[contains(@class,'popover-content')])[1]"
    lastname_err = "(//div[contains(@class,'popover-content')])[2]"
    emailAddr_err = "(//div[contains(@class,'popover-content')])[3]"
    password_err = "(//div[contains(@class,'popover-content')])[4]"
    accesscode_err = "(//div[contains(@class,'popover-content')])[5]"

    # Profile Page
    DOB_txtbox = "#dateOfBirth"
    next_btn = ".btn.btn-primary.carousel-next"
    begin_goalflow_btn = "goal-flow-profile-begin"
    grossAnnualIncome_txtbox = "#grossAnnualIncome"
    Familiar_No_RadioBtn = "#managedPortfolioPreference-1+label"
    Familiar_Yes_RadioBtn = "#managedPortfolioPreference-0+label"

