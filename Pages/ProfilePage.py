from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import locators


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.dob_txtbox_name = locators.DOB_txtbox
        self.nxt_btn = locators.next_btn
        self.login_btn_name = locators.login_btn_name
        self.begin_btn = locators.begin_goalflow_btn
        self.Yes_Radio_Btn = locators.Familiar_Yes_RadioBtn
        self.No_Radio_Btn = locators.Familiar_No_RadioBtn
        self.grossAnnualIncome_txtbox = locators.grossAnnualIncome_txtbox

    def enter_dob(self, dob):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.dob_txtbox_name)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.dob_txtbox_name)))
        self.driver.find_element_by_css_selector(self.dob_txtbox_name).clear()
        self.driver.find_element_by_css_selector(self.dob_txtbox_name).send_keys(dob)

    def enter_grossAnnual_salary(self, grossAnnualSalary):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.grossAnnualIncome_txtbox)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.grossAnnualIncome_txtbox)))
        self.driver.find_element_by_css_selector(self.grossAnnualIncome_txtbox).clear()
        self.driver.find_element_by_css_selector(self.grossAnnualIncome_txtbox).send_keys(grossAnnualSalary)

    def click_next_btn(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.nxt_btn)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.nxt_btn)))
        self.driver.find_element_by_css_selector(self.nxt_btn).click()

    def click_begin_btn(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.begin_btn)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, self.begin_btn)))
        self.driver.find_element_by_id(self.begin_btn).click()

    def click_familiar_Yes_radioBtn(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.Yes_Radio_Btn)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.Yes_Radio_Btn)))
        self.driver.find_element_by_css_selector(self.Yes_Radio_Btn).click()

    def click_familiar_No_radioBtn(self):
        self.driver.find_element_by_css_selector(self.No_Radio_Btn).click()
