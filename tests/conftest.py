import pytest
from base.webdriverfactory import WebDriverFactory
from pages.LoginPage import LoginPage
from pages.NavBar import NavBar
from pages.Archives import ArchivesPage


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    Lp = LoginPage(driver)
    Nb = NavBar(driver)
    Lp.login()
    Nb.goToArchive()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.yield_fixture(scope="function")
def setUp():
    print("Running test set up")
    yield
    ArchivesPage.removeAllFilters()
    print("running test teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")