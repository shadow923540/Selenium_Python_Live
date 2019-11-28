from selenium import webdriver
import os

def singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args,**kwargs)
        return instances[myClass]
    return getInstance

@singleton
class WebDriverFactory():
    driverLocation = "C:\\Python_training\\venv\\Scripts\\chromedriver.exe"
    # driverLocation = "C:\\Users\\Pawel\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation
    driver = webdriver.Chrome(driverLocation)
    def getWebDriverInstance(self):
        return self.driver
