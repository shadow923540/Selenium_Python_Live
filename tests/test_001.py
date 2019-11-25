from pages.page1 import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
import allure

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.Lp = LoginPage(self.driver)

    def test_validLogin(self):
        self.Lp.login()
        result1 = self.Lp.getWelcomeMessage("Welcome to your home page, AgentTestowy!")
        self.ts.markFinal("test_validLogin", result1, "Login was not succesful")
        time.sleep(5)

    def test_empty(self):
        pass

    def test_empyy2(self):
        pass





