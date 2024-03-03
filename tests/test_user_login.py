import time
import pytest

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.login_page import LoginPage
from framework.page import Page
from tests.xpath_elements import Xpath, element_id
from utils.android_utils import get_url, android_get_desired_capabilities
from utils import Loger, get_udid


@pytest.mark.parametrize("expected_output", [
    "Wrong login or password"
])
def test_user_login_negative_case(driver, expected_output: str) -> None:
    try:
        login_instance = LoginPage(driver)
        login_instance.login('qa.ajax.app.automation@gmail.com', 'wrong_pass')
        time.sleep(1)
        login_error = driver.find_element(MobileBy.ID, element_id['login_error'])
        loger = Loger("test_user_login_negative_case", 'Success')
        loger.print(
            f"udid: {get_udid()}, test_user_login_negative_case: result: {login_error.text}, expected: {expected_output}\n")
        assert login_error.text == expected_output
    except Exception as ex:
        loger = Loger("test_user_login_negative_case", 'Failed')
        loger.print(
            f"udid: {get_udid()}, test_user_login_negative_case: exception: {ex}\n")
        assert False


@pytest.mark.parametrize("expected_output", [
    "Add Hub"
])
def test_user_login(driver, expected_output: str) -> None:
    try:
        login_instance = LoginPage(driver)
        login_instance.login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
        time.sleep(10)
        add_hub = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id['add_hub']))
        )
        loger = Loger("test_user_login", 'Success')
        loger.print(f"udid: {get_udid()}, test_user_login: result: {add_hub.text}, expected: {expected_output}\n")
        assert add_hub.text == expected_output
    except Exception as ex:
        loger = Loger("test_user_login", 'Failed')
        loger.print(
            f"udid: {get_udid()}, test_user_login: exception: {ex}\n")
        assert False
