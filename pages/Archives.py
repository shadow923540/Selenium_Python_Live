import utilities.custom_logger as cl
import logging
import allure
import time
from base.basepage import BasePage

class ArchivesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    ################### LOCATORS #####################

    _archives_icon = "a[href='/archives']"
    _archives_text = "css-pbayr1"
    _home_icon = "a[href='/home']"
    _archives_welcome_message = ".css-pbayr1"
    _search_in_archives = "input.css-1qq8djj css-673enp4"
    _add_filter = ".css-rnahou0 > span"
    _chat_authors = "//div[contains(text(), 'and') and contains(@class,'css-1w1vawl')]"

    #Filter options
    _date_field = ".css-1jy8uex > li:nth-child(1) > div > button"
    _agent_field = ".css-1jy8uex > li:nth-child(2) > div > button"
    _rating_field = ".css-1jy8uex > li:nth-child(5) > div > button"
    _tag_field = ".css-1jy8uex > li:nth-child(6) > div > button"

    _show_chats = ".css-aezl7o > button"
    _name_of_tag = '.css-hyz9fq'
    _locators_of_tag = 'css-18zr55l'

    #Date field options
    _date_field_today = ".css-y9xtj8> li:nth-child(1)"
    _date_field_yesterday = ".css-y9xtj8> li:nth-child(2)"
    _date_field_last7days = ".css-y9xtj8> li:nth-child(3)"
    _date_field_last30days = ".css-y9xtj8> li:nth-child(4)"
    _date_field_last_month = ".css-y9xtj8> li:nth-child(5)"
    _date_field_current_month = ".css-y9xtj8> li:nth-child(6)"
    _date_field_check_filter = ".css-v45ci8 > div > span"

    #Agent field options
    _agent_field_1 = ".css-14igyak > li:nth-child(1)"
    _agent_field_2 = ".css-14igyak > li:nth-child(2)"
    _agent_field_1_title = ".css-14igyak > li:nth-child(1) > div > div > div > span:nth-child(1)"
    _agent_field_2_title = ".css-14igyak > li:nth-child(2) > div > div > div > span:nth-child(1)"


    #Rating field options
    _rating_field_any_rating = ".css-14igyak > li:nth-child(1)"
    _rating_field_not_rated = ".css-14igyak > li:nth-child(2)"
    _rating_field_rated_bad = ".css-14igyak > li:nth-child(3)"
    _rating_field_rated_good = ".css-14igyak > li:nth-child(4)"
    _rating_field_rated_and_commented = ".css-14igyak > li:nth-child(5)"
    _rating_field_bad_commented = ".css-14igyak > li:nth-child(6)"
    _rating_field_good_commented = ".css-14igyak > li:nth-child(7)"

    #Tag field options
    _tag_field_not_tagged = ".css-14igyak > li:nth-child(1)"
    _tag_field_complaint = ".css-14igyak > li:nth-child(2)"
    _tag_field_spam = ".css-14igyak > li:nth-child(3)"
    _tag_field_positive_feedback = ".css-14igyak > li:nth-child(4)"
    _tag_field_sales = ".css-14igyak > li:nth-child(5)"
    _tag_field_support = ".css-14igyak > li:nth-child(6)"

    _numbers_of_chats = ".css-1a35ai7 > li"
    _remove_filter = ".remove"
    _clear_all='button.css-vc72rn'

    ################### LOCATORS #####################

    def checkIfUserOnArchivesPage(self):
        self.waitForElementAndCheckText(self._archives_welcome_message, 'css', 'Archives')
    def clickAddFilter(self):
        self.elementClick(self._add_filter)
    def clickDateField(self):
        self.elementClick(self._date_field)
    def clickRatingField(self):
        self.elementClick(self._rating_field)
    def clickAgentField(self):
        self.elementClick(self._agent_field)
    def clickTagField(self):
        self.elementClick(self._tag_field)
    def clickFirstAgent(self):
        self.elementClick(self._agent_field_1)
    def clickRateField(self):
        self.elementClick(self._rating_field)
    def clickRatedBad(self):
        self.elementClick(self._rating_field_rated_bad)
    def getNumbersOfChats(self):
        self.waitUntilElementIsVisible(self._numbers_of_chats, 'css')
        numbers_of_chats = len(self.getElementList(self._numbers_of_chats))
        self.log.info("### Numbers of chat ::  " + str(numbers_of_chats))
        return numbers_of_chats
    def clickDateFieldAndChoseFilter(self, locator, locatorType = 'css'):
        self.clickDateField()
        self.elementClick(locator, locatorType)
    def clickRatingFieldAndChoseFilter(self, locator, locatorType = 'css'):
        self.clickRatingField()
        self.elementClick(locator, locatorType)
    def clickTagFieldAndChoseFilter(self, locator, locatorType = 'css'):
        self.clickTagField()
        self.elementClick(locator, locatorType)
    def checkTextInDateFieldAndButtonText(self, dateText, buttonText):
        time.sleep(1)
        result_1 = self.waitForElementAndCheckText(self._show_chats, 'css', buttonText)
        result_2 = self.waitForElementAndCheckText(self._date_field_check_filter, 'css', dateText)
        result = [result_1, result_2]
        return result
    def checkTextInTagdButtonText(self, buttonText):
        time.sleep(1)
        result= self.waitForElementAndCheckText(self._show_chats, 'css', buttonText)
        return result
    def clearAllFilterAndCheckChatsMessage(self):
        self.elementClick(self._clear_all)
        self.waitForElementAndCheckText(self._show_chats, 'css', "Show all chats")

    def assertResult(self, actual, value):
        if actual == value:
            self.log.info("### VERIFICATION SUCCESSFUL : " + str(actual) + str(value))
            return "PASS"
        else:
            self.log.error("### VERIFICATION FAIL :: Actual value: " + str(actual) + " should be: " + str(value))
            return "FAIL"

    @allure.step("Click each date option in sequence and check text in webelement - button and filtr")
    def checkDateFilter(self):
        self.clickAddFilter()
        self.clickDateFieldAndChoseFilter(self._date_field_today)
        result_1 = self.checkTextInDateFieldAndButtonText('Today', 'Show 0 chats')
        self.clickDateFieldAndChoseFilter(self._date_field_yesterday)
        result_2 = self.checkTextInDateFieldAndButtonText('Yesterday', 'Show 0 chats')
        self.clickDateFieldAndChoseFilter(self._date_field_last7days)
        result_3 = self.checkTextInDateFieldAndButtonText('Last 7 days', 'Show 0 chats')
        self.clickDateFieldAndChoseFilter(self._date_field_last30days)
        result_4 = self.checkTextInDateFieldAndButtonText('Last 30 days', 'Show 0 chats')
        self.clickDateFieldAndChoseFilter(self._date_field_last_month)
        result_5 = self.checkTextInDateFieldAndButtonText('Last month', 'Show 0 chats')
        self.clickDateFieldAndChoseFilter(self._date_field_current_month)
        result_6 = self.checkTextInDateFieldAndButtonText('Current month', 'Show 0 chats')
        self.clearAllFilterAndCheckChatsMessage()
        self.waitUntilElementIsClickable(self._show_chats)
        time.sleep(1)
        self.elementClick(self._show_chats)
        numberOfChats = self.getNumbersOfChats()
        result_7 = self.assertResult(numberOfChats,4)
        result = [result_1, result_2, result_3, result_4, result_5, result_6, result_7]
        return result

    @allure.step("Click each rating option in sequence and check text in webelement - button and filtr")
    def checkRatingFilter(self):
        self.clickAddFilter()
        self.clickRatingFieldAndChoseFilter(self._rating_field_any_rating)
        result_1 = self.checkTextInDateFieldAndButtonText('Any rating', 'Show 3 chats')
        self.clickRatingFieldAndChoseFilter(self._rating_field_not_rated)
        result_2 = self.checkTextInDateFieldAndButtonText('Not rated', 'Show 1 chats')
        self.clickRatingFieldAndChoseFilter(self._rating_field_rated_bad)
        result_3 = self.checkTextInDateFieldAndButtonText('Rated bad', 'Show 1 chats')
        self.clickRatingFieldAndChoseFilter(self._rating_field_rated_good)
        result_4 = self.checkTextInDateFieldAndButtonText('Rated good', 'Show 2 chats')
        self.clickRatingFieldAndChoseFilter(self._rating_field_rated_and_commented)
        result_5 = self.checkTextInDateFieldAndButtonText('Rated & commented', 'Show 2 chats')
        self.clickRatingFieldAndChoseFilter(self._rating_field_bad_commented)
        result_6 = self.checkTextInDateFieldAndButtonText('Rated bad & commented', 'Show 1 chats')
        self.clickRatingFieldAndChoseFilter(self._rating_field_good_commented)
        result_7 = self.checkTextInDateFieldAndButtonText('Rated good & commented', 'Show 1 chats')
        result = [result_1, result_2, result_3, result_4, result_5, result_6, result_7]
        return result

    def checkIfSelectedTagIsVisibleInConversation(self, selectedTag):
        time.sleep(1)
        result = []
        chats = self.getElementList(self._numbers_of_chats)
        for chat in chats:
            tag_text = []
            self.elementClick(element=chat)
            tags = self.getElementList(self._name_of_tag)
            for tag in tags:
                tagName = self.getText(element=tag)
                tag_text.append(tagName)
            if selectedTag in tag_text:
                result.append("PASS")
            else:
                result.append("FAIL")
        return result


    def checkIfFilterWorkCorrectlyinAllConversation(self, locator, tagname):
        self.clickAddFilter()
        self.clickTagFieldAndChoseFilter(locator)
        self.waitUntilElementIsClickable(self._show_chats, 'css')
        time.sleep(2)
        self.elementClick(self._show_chats)
        self.waitUntilElementIsVisible(self._archives_text)
        result = self.checkIfSelectedTagIsVisibleInConversation(tagname)
        return result

    def checkIfSelectedAgentIsVisibleInConversation(self, selectedAgent):
        time.sleep(1)
        result = []
        chats = self.getElementList(self._numbers_of_chats)
        for chat in chats:
            self.elementClick(element=chat)
            agentName = self.getText(self._chat_authors, locatorType='xpath')
            if self.util.verifyTextContains(agentName, selectedAgent):
                result.append("PASS")
            else:
                result.append("FAIL")
        return result

    def checkTagAgentFilter(self, locatorAgent, locatorAgentName):
        self.clickAddFilter()
        self.elementClick(self._agent_field)
        agentName = self.getText(locatorAgentName, locatorType='css')
        self.elementClick(locatorAgent)
        time.sleep(1)
        self.elementClick(self._show_chats)
        result = self.checkIfSelectedAgentIsVisibleInConversation(agentName)
        return result

    @allure.step("Select Agent1 filter tag then check if  in each displayed conversation is Agent1")
    def checkTagAgent1Filter(self):
        result = self.checkTagAgentFilter(self._agent_field_1, self._agent_field_1_title)
        return result

    @allure.step("Select Agent2 filter tag then check if  in each displayed conversation is Agent2")
    def checkTagAgent2Filter(self):
        result = self.checkTagAgentFilter(self._agent_field_2, self._agent_field_2_title)
        return result

    @allure.step("Select Spam filter tag then check if Spam tag exists in each displayed conversation")
    def checkTagSpamFilter(self):
        result = self.checkIfFilterWorkCorrectlyinAllConversation(self._tag_field_spam, 'spam')
        return result

    @allure.step("Select Sales filter tag then check if Spam tag exists in each displayed conversation")
    def checkTagSalesFilter(self):
        result = self.checkIfFilterWorkCorrectlyinAllConversation(self._tag_field_sales, 'sales')
        return result

    @allure.step("Removed all filters")
    def removeAllFilters(self):
        self.elementClick(self._home_icon)
        self.elementClick(self._archives_icon)
        self.clickAddFilter()
        self.clickEveryWebElementOnList(self._remove_filter,locatorType='css')
        self.elementClick(self._home_icon)
        self.elementClick(self._archives_icon)
