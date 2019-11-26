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
        self.Lp = LoginPage(self.driver)
        self.Nb = NavBar(self.driver)
        self.Archives = ArchivesPage(self.driver)

    @pytest.mark.run(order=2)
    def test_navigateToArchive(self):
        self.Nb.clickAchivesIcon()
        self.Archives.checkIfUserOnArchivesPage()

    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test check if user is log in after type correct credentials")
    def test_validLogin(self):
        self.Lp.login()

    @pytest.mark.run(order=3)
    def test_checkTodayFiltr(self):
        self.Archives.checkTodayFilter()






