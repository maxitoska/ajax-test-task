import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from .page import Page
from tests.xpath_elements import Xpath

class LoginPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @staticmethod
    def clear(element: WebElement) -> None | Exception:
        try:
            element.clear()
        except Exception as ex:
            return ex

    @staticmethod
    def send_keys(element: WebElement, value: str) -> None | Exception:
        try:
            element.send_keys(value)
        except Exception as ex:
            return ex

    def login(self, email: str, password: str) -> None:
        self.click_element('xpath', Xpath['ajax_app'])
        time.sleep(3)
        self.click_element('xpath', Xpath['login'])
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Xpath['email_field']))
        )
        self.clear(email_field)
        self.send_keys(email_field, email)
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Xpath['password_field'])))

        self.clear(password_field)
        self.send_keys(password_field, password)
        self.click_element('xpath', Xpath['login_button'])
