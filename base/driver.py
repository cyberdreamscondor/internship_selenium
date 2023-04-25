from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from waits import Wait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import selenium.common.exceptions as exceptions


class Driver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(self.driver, 10)

    def find(self, wait_type, locator_type, loc) -> WebElement:

        types = {
            'css': 'css selector',
            'xpath': 'xpath',
            'id': 'id'
        }
        if locator_type in types:
            loc_type = types[locator_type]
        else:
            raise Exception('Invalid locator type')

        try:
            element = self.wait.wait_for(wait_type, loc_type, loc)
        except exceptions.NoSuchElementException:
            print('Element not found')
        return element

    '''
    # I think this has to be in Base. It is common for any page.
    # nothing to do with driver 
    
    def populate(self, locator_type, loc, text):
        element = self.find('presence_of_element', locator_type, loc)
        element.send_keys(text)
    '''

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def maximize_window(self):
        self.driver.maximize_window()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)