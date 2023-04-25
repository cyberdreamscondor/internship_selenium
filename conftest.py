import pytest
from base.factory import DriverFactory
from pages.login import LoginPage
from pages.dashboard import DashboardPage

@pytest.fixture(scope='class')
def set_up(request):
    """wdf - DriverFactory object to get WebDriver instance for a browser type specified in terminal"""
    browser = request.config.getoption("--browser")
    if browser is None:
        browser = "Chrome"
    wdf = DriverFactory(browser)
    driver = wdf.get_driver()
    dashboard = DashboardPage(driver)


    if request.cls is not None:
        request.cls.driver = driver
        request.cls.dashboard = dashboard

    yield driver
    driver.quit()

# maybe it is better to login via API.
# login page has to be tested separately anyway

@pytest.fixture
def login(set_up):
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    username = 'Admin'
    password = 'admin123'
    login_page = LoginPage(set_up)
    login_page.open_url(BASE_URL)
    login_page.login(username, password)


def pytest_addoption(parser):
    parser.addoption("--browser")
