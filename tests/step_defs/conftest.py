import os

import pytest
from pytest_bdd import given
from selenium import webdriver

citi = 'https://citiwealthbuilderqa.jemstep.com/'
kis = 'https://kisqa.jemstep.com/'


# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, exception):
    print(f'Step Failed: {step}')


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


@pytest.fixture
def browser_chrome():
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(10)
    yield web_driver
    web_driver.close()

#
# @pytest.fixture
# def driver_init_2():
#     web_driver = webdriver.Firefox()
#     web_driver.implicitly_wait(10)
#     yield web_driver
#     web_driver.close()


@given('user is on login page')
def user_is_on_login_page(browser, base_url):
    """user is on login page."""
    browser.get(base_url)


@given('user is on "signup" page')
def user_is_on_login_page(browser, base_url):
    """user is on login page."""
    # assert 200 == urllib.urlopen(base_url).getcode()
    # html = urllib.request.urlopen(base_url).read()
    # print(html)
    browser.get(base_url + "/signup")
