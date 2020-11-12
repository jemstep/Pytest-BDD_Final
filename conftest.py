import pytest
from pytest_base_url.plugin import base_url
from pytest_bdd import given
from selenium import webdriver

citi = 'https://citiwealthbuilderqa.jemstep.com/'
kis = 'https://kisqa.jemstep.com/'


# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, exception):
    print(f'Step Failed: {step}')


# @pytest.fixture
# def browser():
#     b = webdriver.Firefox()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()

#
# @pytest.fixture
# def browsers():
#     print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
#     web_driver = webdriver.Chrome()
#     web_driver.implicitly_wait(10)
#     print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
#     yield web_driver
#     web_driver.close()


def pytest_addoption(parser):
    parser.addoption("-B", "--browsertype",
                     help="Browser type. Available values: chrome, firefox, edge, ie, saucelabs",
                     default="chrome")


def pytest_generate_tests(metafunc):
    if 'browsertype' in metafunc.fixturenames and metafunc.config.option.browsertype is not None:
        metafunc.parametrize("browsertype", [metafunc.config.option.browsertype])


@pytest.fixture
def browser(browsertype):
    """ Creates a webdriver browser instance """
    global browser
    if 'chrome' in browsertype:
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        yield browser
        browser.quit()
    elif 'firefox' in browsertype:
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(firefox_options=options)
        browser.maximize_window()
        browser.implicitly_wait(10)
        yield browser
        browser.quit()
    elif 'ie' in browsertype:
        browser = webdriver.Ie()
        browser.maximize_window()
    elif 'edge' in browsertype:  # Edge is very slow and all steps will throw a timeout error.
        browser_instance = webdriver.Edge()
        browser_instance.maximize_window()
    return browser


@given('user is on login page')
def user_is_on_login_page(base_url):
    """user is on login page."""
    browser.get(base_url)
    browser.implicitly_wait(10)


@given('user is on "signup" page')
def user_is_on_login_page(browser, base_url):
    """user is on login page."""
    # assert 200 == urllib.urlopen(base_url).getcode()
    # html = urllib.request.urlopen(base_url).read()
    # print(html)
    browser.get(base_url + "/signup")
