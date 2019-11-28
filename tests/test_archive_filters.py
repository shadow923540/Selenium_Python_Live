import unittest
import pytest
import allure
from pages.Archives import ArchivesPage
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.Archives = ArchivesPage(self.driver)

    @allure.description("Test check if date filter work correctly and display all chats")
    @pytest.mark.run(order=1)
    def test_checkDateyFiltr(self):
        result = self.Archives.checkDateFilter()
        self.ts.markFinal('CheckTodayFilter', result, "Checkfilter Failed")

    @allure.description("Test check if Spam tag filtr display all conversation with this tag")
    @pytest.mark.run(order=2)
    def test_checkTagSpamFilter(self):
        result = self.Archives.checkTagSpamFilter()
        self.ts.markFinal('CheckSpamFilter', result, "CheckSpamFilter Failed")

    @allure.description("Test check if Sales tag filtr display all conversation with this tag")
    @pytest.mark.run(order=3)
    def test_checkTagSalesFilter(self):
        result = self.Archives.checkTagSalesFilter()
        self.ts.markFinal('CheckSalesFilter', result, "CheckSalesFilter Failed")

    @allure.description("Test check if rate filter work correctly and display all chats")
    @pytest.mark.run(order=4)
    def test_checkRatingFiltrDisplay(self):
        result = self.Archives.checkRatingFilter()
        self.ts.markFinal('CheckAllRatingFilter', result, "Checkfilter Failed")



