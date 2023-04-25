from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\\chromedriver.exe")


class DriverFactory:
    def __init__(self, browser_type):
        self.browser_type = browser_type

    def get_driver(self):
        """Returns WebDriver instance based on browser_type"""
        if self.browser_type.lower() == "chrome":
            driver = webdriver.Chrome()
        elif self.browser_type.lower() == "ff":
            driver = webdriver.Firefox()

        return driver










