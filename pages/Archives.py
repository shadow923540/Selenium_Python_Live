import utilities.custom_logger as cl
import logging

from base.basepage import BasePage
import allure
import time

class ArchivesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        # self.util = Util()


    ################### LOCATORS #####################

    _archives_icon= "a[href='/archives']"
    _home_icon= "a[href='/home']"
    _archives_welcome_message = ".css-pbayr1"
    _search_in_archives = "input.css-1qq8djj css-673enp4"
    _add_filter = ".css-rnahou0 > span"

    #Filter options
    _date_field = ".css-1jy8uex > li:nth-child(1) > div > button"
    _agent_field = ".css-1jy8uex > li:nth-child(2) > div > button"
    _rating_field = ".css-1jy8uex > li:nth-child(5) > div > button"
    _tag_field = ".css-1jy8uex > li:nth-child(6) > div > button"

    _show_chats = ".css-aezl7o > button"

    #Date field options
    _date_field_today = ".css-y9xtj8> li:nth-child(1)"
    _date_field_yesterday = ".css-y9xtj8> li:nth-child(2)"
    _date_field_last7days = ".css-y9xtj8> li:nth-child(3)"
    _date_field_last30days = ".css-y9xtj8> li:nth-child(4)"
    _date_field_last_month = ".css-y9xtj8> li:nth-child(5)"
    _date_field_current_month = ".css-y9xtj8> li:nth-child(6)"

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
    _rating_field_rated_bad_commented = ".css-14igyak > li:nth-child(5)"
    _rating_field_good_commented =  ".css-14igyak > li:nth-child(6)"

    #Tag field options
    _tag_field_not_tagged = ".css-14igyak > li:nth-child(1)"
    _tag_field_complaint = ".css-14igyak > li:nth-child(2)"
    _tag_field_spam = ".css-14igyak > li:nth-child(3)"
    _tag_field_positive_feedback = ".css-14igyak > li:nth-child(4)"
    _tag_field_sales = ".css-14igyak > li:nth-child(5)"
    _tag_field_support = ".css-14igyak > li:nth-child(6)"

    _numbers_of_chats = ".css-1a35ai7 > li"
    _remove_filter = ".remove"

    ################### LOCATORS #####################

    def checkIfUserOnArchivesPage(self):
        self.waitForElementAndCheckText(self._archives_welcome_message, 'css', 'Archives')

    def clickAddFilter(self):
        self.elementClick(self._add_filter)
    def clickDateField(self):
        self.elementClick(self._date_field)
    def clickTodayField(self):
        self.elementClick(self._date_field_today)
    def clickAgentField(self):
        self.elementClick(self._agent_field)
    def clickFirstAgent(self):
        self.elementClick(self._agent_field_1)
    def clickRateField(self):
        self.elementClick(self._rating_field)
    def clickRatedBad(self):
        self.elementClick(self._rating_field_rated_bad)
    def getNumbersOfChats(self):
        numbers_of_chats = len(self.getElementList(self._numbers_of_chats))
        return numbers_of_chats

    def checkTodayFilter(self):
        self.clickAddFilter()
        self.clickDateField()
        self.clickTodayField()
        self.clickRateField()
        self.clickRatedBad()
        time.sleep(2)
        self.removeAllFilters()
        time.sleep(2)

    def removeAllFilters(self):
        self.elementClick(self._home_icon)
        self.elementClick(self._archives_icon)
        self.clickAddFilter()
        self.clickEveryWebElementOnList(self._remove_filter,locatorType='css')
        self.elementClick(self._home_icon)
        self.elementClick(self._archives_icon)
