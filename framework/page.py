from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from typing import Union

class Page:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def find_element(self, by: str, path: str) -> Union[WebElement, Exception]:
        try:
            if by == 'xpath':
                return self.driver.find_element(MobileBy.XPATH, path)
            elif by == 'id':
                return self.driver.find_element(MobileBy.ID, path)
        except Exception as ex:
            return ex

    def click_element(self, by: str, path: str) -> Union[None, Exception]:
        try:
            element = self.find_element(by, path)
            element.click()
        except Exception as ex:
            return ex
