import utilities.custom_logger as cl
import logging
from utilities.util import Util
from base.basepage import BasePage
import allure

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.util = Util()

    # Locators
    _email_field = "email"
    _password_field = "password"
    _login_button = "//div[@class='form']/form/div[3]/button"
    _welcome_message = "//h1[contains(text(), 'Welcome')]"

    email = "m.debski+frontend_tests@livechatinc.com"
    password = "test1@3$"

    @allure.step("Type into EmailField")
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    @allure.step("Type into passwordField")
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    @allure.step("Click LoginButton")
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='xpath')

    def login(self, email= email , password = password):
        self.waitForElement(self._email_field)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    @allure.step("Wait for welcomeMessage after login and save message to variable")
    def getWelcomeMessage(self, welcomeMessageToVerify):
        self.waitForElement(self._welcome_message, locatorType='xpath')
        welcomeMessage = self.getText(self._welcome_message, locatorType='xpath')
        result = self.util.verifyTextMatch(welcomeMessage, welcomeMessageToVerify)
        return result

