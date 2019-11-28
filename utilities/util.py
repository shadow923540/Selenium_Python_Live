import utilities.custom_logger as cl
import logging

class Util():

    log = cl.customLogger(logging.INFO)


    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual Text  --> :: " + actualText)
        self.log.info("Expected Text  --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual Text --> :: " + actualText)
        self.log.info("Expected Text  --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT MATCHED !!!")
            return False

