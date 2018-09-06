from page.base_page import BasePage
from common.locators import MainLocators
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from page.balance_page import BalancePage
from page.acct_statement_page import AccountStatementPage
from page.trans_history_page import TransactionHistoryPage


class MainPage(BasePage):

    def verifyPage(self):
        alert = self.isAlertPresent()
        if alert == True:
            return False

        self.driver.switch_to.default_content()
        return self.getElement(MainLocators.MENU_FRAME) is not None

    def isAlertPresent(self):
        # check if wrong username/password popup is open
        try:
            alert = self.driver.switch_to_alert()
            print("alert popup: {0}".format(alert.text))
            alert.accept()
            return True
        except NoAlertPresentException:
            return False

    def __backToParentMenu(self):
        self.__switchToMenuFrame()
        # check if we're already in parent (has logout link)
        if self.getElement(MainLocators.MENU_LOGOUT) == None:
            self.getElement(MainLocators.MENU_BACK_TO_HOME).click()

    def __clickMenuAccountInformation(self):
        self.__backToParentMenu()
        self.getElement(
            MainLocators.MENU_ACCOUNT_INFORMATION).click()

    def __switchToMenuFrame(self):
        self.driver.switch_to.default_content()
        frame = self.getElement(MainLocators.MENU_FRAME)
        self.driver.switch_to.frame(frame)

    def __switchToContentFrame(self):
        self.driver.switch_to.default_content()
        frame = self.getElement(MainLocators.CONTENT_FRAME)
        self.driver.switch_to.frame(frame)

    def clickMenuBalanceInquiry(self):
        self.__clickMenuAccountInformation()
        self.getElement(MainLocators.SUBMENU_BALANCE_INQUIRY).click()

        self.__switchToContentFrame()
        return BalancePage(self.driver)

    def clickMenuAccountStatement(self):
        self.__clickMenuAccountInformation()
        self.getElement(MainLocators.SUBMENU_ACCOUNT_STATEMENT).click()

        self.__switchToContentFrame()
        return AccountStatementPage(self.driver)

    def clickLogout(self):
        self.__backToParentMenu()
        self.getElement(MainLocators.MENU_LOGOUT).click()

    def clickMenuTransactionHistory(self):
        self.__backToParentMenu()
        self.getElement(MainLocators.MENU_TRANSACTION_HISTORY).click()

        self.__switchToContentFrame()
        return TransactionHistoryPage(self.driver)
