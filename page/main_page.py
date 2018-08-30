from page.base_page import BasePage
from common.locators import MainLocators
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException


class MainPage(BasePage):

    def verifyPage(self):
        alert = self.isAlertPresent()
        if alert is not None:
            return False

        menu = self.driver.find_element(*MainLocators.MENU_FRAME)
        return menu is not None

    def isAlertPresent(self):
        # check if wrong username/password popup is open
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
            return True
        except NoAlertPresentException:
            return False
