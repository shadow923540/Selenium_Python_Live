from selenium import webdriver
import os

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://accounts.labs.livechatinc.com"
        if self.browser == "chrome":
            # driverLocation = "C:\\Python_training\\venv\\Scripts\\chromedriver.exe"
            driverLocation = "C:\\Users\\Pawel\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\Python_training\\venv\\Scripts\\geckodriver.exe")
        elif self.browser == "iexplorer":
            driverLocation = "C:\\Python_training\\venv\\Scripts\\IEDriverServer.exe"
            # driverLocation = "C:\\Users\\Pawel\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\chromedriver.exe"
            os.environ["webdriver.ie.driver"] = driverLocation
            driver = webdriver.Ie(driverLocation)
        else:
            driverLocation = "C:\\Python_training\\venv\\Scripts\\chromedriver.exe"
            # driverLocation = "C:\\Users\\Pawel\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        return driver