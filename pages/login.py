import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from base.driver import Driver
from base.base import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS: uppercase bad idea?
    LOGIN_BUTTON = '.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button'
    USERNAME_FIELD = ".oxd-input.oxd-input--active[name='username']"
    PWD_FIELD = ".oxd-input.oxd-input--active[name='password']"

    # PAGE METHODS
    def click_login_button(self):
        self.find('presence_of_element', "css", self.LOGIN_BUTTON).click()

    def enter_username(self, username):
        self.type("css", self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type("css", self.PWD_FIELD, password)

    def login(self, name, pwd):
        self.wait.wait_for(wait_type='page_load')
        pwd_field = self.find('clickable', 'css', self.PWD_FIELD)
        pwd_field.send_keys(pwd)

        username_field = self.find('clickable', 'css', self.USERNAME_FIELD)
        username_field.send_keys(name)

        self.click_login_button()






