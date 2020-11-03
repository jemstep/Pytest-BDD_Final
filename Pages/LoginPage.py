from Locators.locators import locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_txtbox_name = locators.email_txtbox_name
        self.pass_txtbox_name = locators.pass_txtbox_name
        self.login_btn_name = locators.login_btn_name

    def enter_email(self, email):
        self.driver.find_element_by_css_selector(self.email_txtbox_name).clear()
        self.driver.find_element_by_css_selector(self.email_txtbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.pass_txtbox_name).clear()
        self.driver.find_element_by_css_selector(self.pass_txtbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_name).click()
