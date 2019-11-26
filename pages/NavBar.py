import utilities.custom_logger as cl
import logging
from utilities.util import Util
from base.basepage import BasePage
import allure


class NavBar(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.util = Util()

    # Locators
    _archives_icon= "a[href='/archives']"
    _home_icon= "a[href='/home']"
    _tickets_icon= "a[href='/tickets']"
    _archives_welcome_message = ".css-pbayr1"

    @allure.step('Click archive icon')
    def clickAchivesIcon(self):
        self.elementClick(self._archives_icon)

    def checkIfUserOnArchivesPage(self):
        self.waitForElementAndCheckText(self._archives_welcome_message, 'css', 'Archives')

    def goToArchive(self):
        self.clickAchivesIcon()
        self.checkIfUserOnArchivesPage()
