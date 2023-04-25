from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
import time


class Wait:
    def __init__(self, driver, latency):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, latency)

    def wait_for(self, wait_type=None, loc_type=None, loc=None, text=None):
        """ monster wait function just for fun. I would probably divide it into several custom functions
        when necessary. For now just exploring different wait conditions """

        if wait_type == 'element_selected':
            result = self.wait.until(conditions.element_to_be_selected((loc_type, loc)))
        elif wait_type == 'visibility_of_element':
            result = self.wait.until(conditions.visibility_of_element_located((loc_type, loc)))
        elif wait_type == 'presence_of_all_elements':
            result = self.wait.until(conditions.presence_of_all_elements_located((loc_type, loc)))
        elif wait_type == 'presence_of_element':
            result = self.wait.until(conditions.presence_of_element_located((loc_type, loc)))
        elif wait_type == 'text_to_be_present_in_element':
            result = self.wait.until(conditions.text_to_be_present_in_element((loc_type, loc), "txt"))
        elif wait_type == 'title_contains':
            result = self.wait.until(conditions.title_contains("title"))
        elif wait_type == 'title_is':
            result = self.wait.until(conditions.title_is("title"))
        elif wait_type == 'visibility_of':
            element = self.driver.find_element(loc_type, loc)
            result = self.wait.until(conditions.visibility_of(element))
        elif wait_type == 'alert_is_present':
            result = self.wait.until(conditions.alert_is_present())
        elif wait_type == 'staleness_of':
            element = self.wait.until(conditions.presence_of_element_located((loc_type, loc)))
            result = self.wait.until(conditions.staleness_of(element))
        elif wait_type == 'page_load':
            result = self.wait.until(conditions.presence_of_element_located(('xpath', '//body')))
        elif wait_type == 'text_in_url':
            result = self.wait.until(conditions.url_contains(text))
        elif wait_type == 'clickable':
            result = self.wait.until(conditions.element_to_be_clickable((loc_type, loc)))
        else:
            raise ValueError(f'Invalid wait_type argument: {wait_type}')

        return result












