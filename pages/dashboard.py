from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from base.base import Base
from waits import Wait
from selenium.webdriver.support.ui import Select
import time
import pytest
from selenium.webdriver.common.by import By

class DashboardPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

# these functions assume clicking, checking innerText, sending keys
# currently not used in tests, because there were was more difficult stuff for me to figure out


# punch out
# punch in

