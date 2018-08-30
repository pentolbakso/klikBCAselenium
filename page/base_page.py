from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            print("Unable to find_element - {0}".format(locator))
            return None
