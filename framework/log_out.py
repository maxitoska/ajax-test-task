import time
from .page import Page
from tests.xpath_elements import Xpath, element_id
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class LogoutPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def logout(self) -> WebElement:
        self.click_element('xpath', Xpath['ajax_app'])
        time.sleep(1)
        self.click_element('id', element_id['menu'])
        time.sleep(1)
        self.click_element('id', element_id['app_settings'])
        time.sleep(1)
        self.click_element('xpath', Xpath['logout'])
        time.sleep(5)
        return self.find_element('xpath', Xpath['create_account'])
