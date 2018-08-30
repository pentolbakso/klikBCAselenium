from page.base_page import BasePage
from common.locators import LoginLocators
from page.main_page import MainPage


class LoginPage(BasePage):

    def fillUserID(self, userid):
        self.driver.find_element(*LoginLocators.USERID_FIELD).send_keys(userid)

    def fillPassword(self, password):
        self.driver.find_element(
            *LoginLocators.PASSWORD_FIELD).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        return MainPage(self.driver)

    def verifyPage(self):
        return "klikBCA" in self.driver.title

    def launchUrl(self, url):
        self.driver.get(url)
