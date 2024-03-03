import time
import pytest

from typing import Any
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.xpath_elements import (
    Xpath,
    side_bar_buttons_xpath,
    side_bar_buttons_id,
    element_id
)
from utils import Loger, get_udid


@pytest.mark.parametrize("expected_output", [
    "Copied"
])
def test_sidebar(driver, expected_output: str):
    try:
        driver.press_keycode(3)
        driver.find_element(MobileBy.XPATH, Xpath['ajax_app']).click()
        time.sleep(5)
        driver.find_element(MobileBy.ID, element_id['menu']).click()
        time.sleep(3)
        for xpath in side_bar_buttons_xpath.values():
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))).is_enabled()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, side_bar_buttons_id['terms_of_service']))).is_enabled()

        driver.find_element(MobileBy.ID, side_bar_buttons_id['build']).click()
        element = driver.find_element(MobileBy.ID, side_bar_buttons_id['build_message'])
        loger = Loger("test_sidebar", 'Success')
        loger.print(f"udid: {get_udid()}, test_sidebar: result: {element.text}, expected: Copied")

        assert element.text == expected_output
    except Exception as ex:
        loger = Loger("test_sidebar", 'Failed')
        loger.print(f"udid: {get_udid()}, test_sidebar: exception: {ex}")
        assert False
