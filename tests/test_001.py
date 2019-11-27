from pages.LoginPage import LoginPage
from pages.NavBar import NavBar
from pages.Archives import ArchivesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import allure
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.Archives = ArchivesPage(self.driver)

    # @pytest.mark.run(order=1)
    # def test_checkTodayFiltr(self):
    #     result = self.Archives.checkDaysFilter()
    #     print(result)
    #     self.ts.markFinal('CheckTodayFilter', result, "Checkfilter Failed")

    @pytest.mark.run(order=1)
    def test_checkSpamFilter(self):
        result = self.Archives.checkIfSpamFilterWorkCorrectly()
        print(result)
        self.ts.markFinal('CheckSpamFilter', result, "CheckSpamFilter Failed")





