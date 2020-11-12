# coding=utf-8
"""Login to citiwealthbuilder and fill RTQs feature tests."""
import random
import time
import json

import pytest
from pytest_bdd import (
    then,
    when, parsers, scenario,
)

from Pages.LoginPage import LoginPage
from Pages.SignupPage import SignupPage


# @pytest.mark.usefixtures("browser")
# @pytest.mark.order1
@pytest.mark.usefixtures("browser")
@scenario('../features/signup.feature', 'Signup into Blue Application')
@scenario('../features/signup.feature', 'Signup into Blue Application - Negative')
def test_signup_into_blue_application():
    """Signup into Blue Application."""


@when('enters <accessCode>')
def enters_accesscode(accessCode, browser):
    """enters <accessCode>."""
    signup = SignupPage(browser)
    signup.enter_accessCode(accessCode)


@when('user enters <LastName>')
def user_enters_lastname(LastName, browser):
    """user enters <LastName>."""
    signup = SignupPage(browser)
    signup.enter_lastName(LastName)


@when('user enters <emailAddress>')
def user_enters_emailaddress(emailAddress, browser):
    """user enters <emailAddress>."""
    signup = SignupPage(browser)
    newEmail = emailAddress.split("@")
    newMail = newEmail[0] + str(random.randint(1, 1000))
    mail = newMail + "@" + newEmail[1]
    # Data to be written
    dictionary = {
        "email": mail,
    }
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("TestData/testdata.json", "w") as outfile:
        outfile.write(json_object)
    signup.enter_email(mail)


@when('user enters <firstName>', )
def user_enters_firstname(firstName, browser):
    """user enters <firstName>."""
    signup = SignupPage(browser)
    signup.enter_firstName(firstName)


@when('user enters <password>')
def user_enters_password(password, browser):
    """user enters <password>."""
    signup = SignupPage(browser)
    signup.enter_password(password)
    # # Data to be written
    # dictionary = {
    #     "password": password,
    # }
    # # Serializing json
    # json_object = json.dumps(dictionary, indent=4)
    #
    # # Writing to sample.json
    # with open("TestData/testdata.json", "w") as outfile:
    #     outfile.write(json_object)


@then('user clicks on "Signup" button')
def user_clicks_on_signup_button(browser):
    """user clicks on "Signup" button."""
    time.sleep(5)
    signup = SignupPage(browser)
    signup.click_signup()


@when('user clicks on "Signup" button')
def user_clicks_on_signup_button(browser):
    """user clicks on "Signup" button."""
    signup = SignupPage(browser)
    signup.click_signup()


@then(parsers.cfparse('user verifies "{title}" title is displayed'))
def user_verifies__citi_wealth_builder__investor_profile_title_is_displayed(browser, title):
    """user verifies " Citi Wealth Builder - Investor Profile" title is displayed."""
    assert title == browser.title


@then(parsers.cfparse('user verifies "{title}" title is not displayed'))
def user_verifies__citi_wealth_builder__investor_profile_title_is_not_displayed(browser, title):
    """user verifies " Citi Wealth Builder - Investor Profile" title is not displayed."""
    assert title != browser.title


@then(parsers.cfparse('user sees page title as "{title}"'))
def user_sees_page_title_as_citi_wealth_builder__investor_profile(browser, title):
    """user sees page title as "Citi Wealth Builder - Investor Profile"."""
    assert title == browser.title


@then(parsers.cfparse('user sees error message as "{title}" for "{name}" field'))
def user_sees_error_message_as_must_be_at_least_10_characters_long_must_contain_at_least_one_lowercase_and_uppercase_character_must_contain_at_least_one_number_must_contain_at_least_one_special_character_eg(
        browser, title, name):
    """user sees error message as "Must be at least 10 characters long Must contain at least one lowercase and
    uppercase character Must contain at least one number Must contain at least one special character e.g. '! @. """
    signup = SignupPage(browser)
    actualTitle = signup.err_validations(name)
    assert title == actualTitle


@when('user clicks on "login"')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    # browser.find_element_by_id('btn-login').click()
    login = LoginPage(browser)
    login.click_login()


@when(parsers.cfparse('user enters "{emailText}" as "{value}" and "{passwordText}" as "{password}"'))
def user_enters_email_as__and_password_as_(browser, value, password):
    """user enters "email" as "" and password as ""."""
    login = LoginPage(browser)
    login.enter_email(value)
    login.enter_password(password)


@then(parsers.cfparse('user sees page title as "{title}"'))
def user_sees_home_page(browser, title):
    """user sees "Home page"."""

    assert title == browser.title


@then(parsers.cfparse('user sees error message as "{title}"'))
def user_sees_error_message(browser, title):
    """user sees "Error message"."""

    assert title == browser.find_element_by_class_name('alert-danger__paragraph').text


@then(parsers.cfparse('user sees error message as "{title}" for "{name}" field'))
def user_sees_error_message(browser, title, name):
    """user sees "Error message for name fields"."""

    signup = SignupPage(browser)
    signup.click_all()
    actualTitle = signup.err_validations(name)
    assert title == actualTitle


@then(parsers.cfparse('user sees error message as "{title}" for "{name}" field'))
def user_sees_error_message(browser, title, name):
    """user sees "Error message for name fields"."""

    signup = SignupPage(browser)
    signup.click_all()
    actualTitle = signup.err_validations(name)
    assert title == actualTitle


@then('user waits for page load')
def user_waits_for_page_load():
    """user waits for page load."""
    time.sleep(5)
