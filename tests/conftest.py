import subprocess
import time
from typing import Any

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server() -> None:
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server: Any) -> WebDriver:
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    driver.press_keycode(3)
    yield driver
    driver.quit()
