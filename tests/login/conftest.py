import pytest
from framework.login_page import LoginPage
from appium.webdriver.webdriver import WebDriver

@pytest.fixture(scope='function')
def user_login_fixture(driver: WebDriver) -> LoginPage:
    yield LoginPage(driver)
