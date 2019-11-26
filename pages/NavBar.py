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

    @allure.step('Click archive icon')
    def clickAchivesIcon(self):
        self.elementClick(self._archives_icon)

