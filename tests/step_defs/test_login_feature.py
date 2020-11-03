# coding=utf-8
"""Login feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers, scenarios,
)


@scenario('../features/login.feature', 'Login to cwb with valid credentials')
@scenario('../features/login.feature', 'Login to cwb with invalid credentials')
#scenarios('../features')

def test_login_to_cwb():
    """Login to cwb."""


@when('user clicks on "login"')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    browser.find_element_by_id('btn-login').click()


@when(parsers.cfparse('user enters "{emailText}" as "{value}" and "{passwordText}" as "{password}"'))
def user_enters_email_as__and_password_as_(browser, value, password):
    """user enters "email" as "" and password as ""."""
    browser.find_element_by_css_selector('#emailAddress').send_keys(value)
    browser.find_element_by_css_selector('#password').send_keys(password)


@then(parsers.cfparse('user sees page title as "{title}"'))
def user_sees_home_page(browser, title):
    """user sees "Home page"."""

    assert title == browser.title


@then(parsers.cfparse('user sees error message as "{title}"'))
def user_sees_error_message(browser, title):
    """user sees "Error message"."""

    assert title == browser.find_element_by_class_name('alert-danger__paragraph').text