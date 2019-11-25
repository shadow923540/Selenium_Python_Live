from pages.LoginPage import LoginPage
from pages.NavBar import NavBar
from utilities.teststatus import TestStatus
import unittest
import pytest
import allure

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.Lp = LoginPage(self.driver)
        self.Nb = NavBar(self.driver)

    @pytest.fixture()
    def navigateToArchive(self):
        pass


    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test check if user is log in after type correct credentials")
    def test_validLogin(self):
        self.Lp.login()
        result1 = self.Lp.getWelcomeMessage("Welcome to your home page, AgentTestowy!")
        self.ts.markFinal("test_validLogin", result1, "Login was not succesful")

    def test_empty(self):
        pass

    def test_empyy2(self):
        pass





