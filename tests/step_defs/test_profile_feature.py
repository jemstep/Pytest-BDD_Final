# coding=utf-8
"""Login to CWB and fill profile questionnaire feature tests."""
import time
import json

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)

from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage


#@pytest.mark.order2
@scenario('../features/profile.feature', 'Fill Profile questionnaire')
def test_fill_profile_questionnaire():
    """Fill Profile questionnaire."""


@when('user clicks on "Begin"')
def user_clicks_on_begin(browser):
    """user clicks on "Begin"."""
    time.sleep(2)
    profile = ProfilePage(browser)
    profile.click_begin_btn()


@then('user clicks on "Next question"')
def user_clicks_on_next_question(browser):
    """user clicks on "Next question"."""
    profile = ProfilePage(browser)
    profile.click_next_btn()


@then(parsers.cfparse('user enters "DOB" as "{dob}"'))
def user_enters_dob_as_01011995(browser, dob):
    """user enters "DOB" as "01011995"."""
    profile = ProfilePage(browser)
    profile.enter_dob(dob)


@when(parsers.cfparse('user enters "{emailText}" as "{value}" and "{passwordText}" as "{password}"'))
def user_enters_email_as__and_password_as_(browser, value, password):
    """user enters "email" as "" and password as ""."""

    # Opening JSON file
    with open('TestData/testdata.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    print(json_object['email'])
    # print(type(json_object))

    login = LoginPage(browser)
    login.enter_email(json_object['email'])
    login.enter_password(password)


@then(parsers.cfparse('user sees page title as "{title}"'))
def user_sees_home_page(browser, title):
    """user sees "Home page"."""
    time.sleep(2)
    assert title == browser.title


@when('user clicks on "login"')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    login = LoginPage(browser)
    login.click_login()


@then('user waits for page load')
def user_waits_for_page_load():
    """user waits for page load."""
    time.sleep(5)


@when('user selects Investment experience as "Yes"')
def user_selects_investment_experience_as_yes(browser):
    """user selects Investment experience as "Yes"."""
    profile = ProfilePage(browser)
    profile.click_familiar_Yes_radioBtn()


@then(parsers.cfparse('user enters "Gross Annual Salary" as "{value}"'))
def user_enters_gross_annual_salary_as_100000(browser, value):
    """user enters "Gross Annual Salary" as "100000"."""
    profile = ProfilePage(browser)
    profile.enter_grossAnnual_salary(value)


@then(parsers.cfparse('user sees page title as "{title}"'))
def user_sees_page_title_as_citi_wealth_builder__goals(browser, title):
    """user sees page title as "Citi Wealth Builder - Goals"."""
    time.sleep(2)
    assert title == browser.title
