from base.driver import Driver
from waits import Wait


class Base(Driver):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_url(self, url):
        assert self.driver.current_url == url

    def verify_title(self, title):
        assert self.driver.title() == title

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator_type, loc):
        element = self.find('clickable', locator_type, loc)
        element.click()

    def type(self, locator_type, loc, text):
        element = self.find('visibility_of', locator_type, loc)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator_type, loc, exp_text):
        element = self.find('visibility_of', locator_type, loc)
        self.wait.wait_for('text_to_be_present_in_element', locator_type, loc, text=exp_text)
        return element.text

    def scroll_to_element(self, locator_type, loc):
        element = self.find('presence_of_element', locator_type, loc)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_to_frame(self, locator_type, loc):
        element = self.find('presence_of_element', locator_type, loc)
        self.driver.switch_to.frame(element)





