import pytest
from base.webdriverfactory import WebDriverFactory
from pages.LoginPage import LoginPage
from pages.NavBar import NavBar
from pages.Archives import ArchivesPage


def getDriver():
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()
    return driver

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    baseUrl = "https://accounts.labs.livechatinc.com"
    driver = getDriver()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseUrl)
    Lp = LoginPage(driver)
    Nb = NavBar(driver)
    Lp.login()
    Nb.goToArchive()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setUp():
    driver = getDriver()
    Archive = ArchivesPage(driver)
    Archive.removeAllFilters()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")