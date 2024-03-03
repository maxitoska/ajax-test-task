import pytest

from framework.log_out import LogoutPage
from framework.page import Page
from utils.android_utils import get_url, android_get_desired_capabilities
from utils import Loger, get_udid


@pytest.mark.parametrize("expected_output", [
    "Create Account"
])
def test_user_logout(driver, expected_output: str) -> None:
    try:
        logout_instance = LogoutPage(driver)
        login_button_text = logout_instance.logout()
        loger = Loger("test_user_logout", 'Success')
        loger.print(
            f"udid: {get_udid()}, test_user_logout: result: {login_button_text.text}, expected: {expected_output}")
        assert login_button_text.text == expected_output
    except Exception as ex:
        loger = Loger("test_user_logout", 'Failed')
        loger.print(
            f"udid: {get_udid()}, test_user_logout: exception: {ex}"
        )
        assert False
