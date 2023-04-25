import pytest
from selenium.webdriver.common.by import By
from pages.dashboard import DashboardPage
from pages.login import LoginPage
import time


class TestDashboard:
    def test_login(self, login):
        """ Just login, not going to test it here """
        pass

    # LOCATORS
    widgets_list = '.orangehrm-dashboard-widget-name p'
    widget_elements = {
        "employee_img": '.employee-image',
        "big_stopwatch": '.oxd-icon-button.oxd-icon-button--solid-main.orangehrm-attendance-card-action',
        "small_stopwatch": '.oxd-text.oxd-text--p.orangehrm-attendance-card-fulltime',
        "hours_today": '.oxd-text.oxd-text--span.orangehrm-attendance-card-fulltime',
        "chart": '.emp-attendance-chart'
    }

    def test_all_widget_presence(self, set_up):
        """ Checks all widgets presence and titles """
        expected_widget_names = ['Time at Work', 'My Actions', 'Quick Launch',
                                 'Buzz Latest Posts', 'Employees on Leave Today',
                                 'Employee Distribution by Sub Unit', 'Employee Distribution by Location']
        widgets_located = self.dashboard.find('presence_of_all_elements', 'css', self.widgets_list)
        widget_names_located = []
        for widget in widgets_located:
            widget_names_located.append(widget.get_attribute("innerText"))
        assert widget_names_located == expected_widget_names

    def test_widget_elements_displayed(self,set_up):
        """ Checks all widget elements displayed. Find function contains
            necessary exceptions handling. """
        # but what if I would like to have a list of elements that were not found?
        # what if I don't want to interrupt the cycle

        elements_located = []
        elements_missing = []
        for element, locator in self.widget_elements.items():
            elem_located = self.dashboard.find('presence_of_element', 'css', locator)
            if elem_located is not None:
                elements_located.append(elem_located)
            else:
                elements_missing.append(locator)
        assert len(elements_located) == len(list(self.widget_elements.values()))
        assert not elements_missing, f"Following elements were not found: {elements_missing}"


    def test_widget_onwindowresize(self, set_up):
        pass

    ### At his stage project contains most of the stuff I know, tried to explore, had difficulties with.
    ### Sending keys, making screenshots, using calendar, finding elements... it's all cool
    ###(and I did this in homeworks),  but I am MUCH MORE afraid of the interview and
    ### since all of this code is written by me solely, temporarily pause this project :)












