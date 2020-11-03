from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import locators


class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.firstName_Txtbox = locators.firstname_txtbox
        self.lastName_Txtbox = locators.lastname_txtbox
        self.password_Txtbox = locators.password_txtbox
        self.accessCode = locators.accessCode_txtbox
        self.emailAddr = locators.emailAddr_txtbox
        self.signupBtn = locators.signup_btn
        self.firstNameErr = locators.firstname_err
        self.lastNameErr = locators.lastname_err
        self.emailAddrErr = locators.emailAddr_err
        self.passwordErr = locators.password_err
        self.accesscodeErr = locators.accesscode_err

    def enter_email(self, email):
        self.driver.find_element_by_css_selector(self.emailAddr).clear()
        self.driver.find_element_by_css_selector(self.emailAddr).send_keys(email)

    def enter_firstName(self, email):
        self.driver.find_element_by_css_selector(self.firstName_Txtbox).clear()
        self.driver.find_element_by_css_selector(self.firstName_Txtbox).send_keys(email)

    def enter_lastName(self, email):
        self.driver.find_element_by_css_selector(self.lastName_Txtbox).clear()
        self.driver.find_element_by_css_selector(self.lastName_Txtbox).send_keys(email)

    def enter_accessCode(self, email):
        self.driver.find_element_by_css_selector(self.accessCode).clear()
        self.driver.find_element_by_css_selector(self.accessCode).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.password_Txtbox).clear()
        self.driver.find_element_by_css_selector(self.password_Txtbox).send_keys(password)

    def click_all(self):
        self.driver.find_element_by_css_selector(self.firstName_Txtbox).click()
        self.driver.find_element_by_css_selector(self.lastName_Txtbox).click()
        self.driver.find_element_by_css_selector(self.accessCode).click()
        self.driver.find_element_by_css_selector(self.password_Txtbox).click()
        self.driver.find_element_by_css_selector(self.emailAddr).click()

    def click_signup(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.signupBtn)))
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, self.signupBtn)))
        element.click()

        # self.driver.execute_script("arguments[0].click();", element)

    def err_validations(self, name):
        if "first" in name:
            titles = self.driver.find_element_by_xpath(self.firstNameErr).text
            # print("YAHOOO" +titles)
            return titles
        elif "last" in name:
            titles = self.driver.find_element_by_xpath(self.lastNameErr).text
            return titles
        elif "email" in name:
            titles = self.driver.find_element_by_xpath(self.emailAddrErr).text
            return titles
        elif "pass" in name:
            titles = self.driver.find_element_by_xpath(self.passwordErr).text
            print("YIPIEEE" +titles)
            return titles
        elif "access" in name:
            titles = self.driver.find_element_by_xpath(self.accesscodeErr).text
            return titles

    def wait_until_clickable(self, element):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, element)))
        element.click()
