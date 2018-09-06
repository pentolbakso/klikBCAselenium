from selenium.webdriver.common.by import By


class LoginLocators(object):
    USERID_FIELD = (By.ID, "user_id")
    PASSWORD_FIELD = (By.ID, "pswd")
    LOGIN_BUTTON = (By.NAME, "value(Submit)")


class MainLocators(object):
    MENU_FRAME = (By.NAME, "menu")
    CONTENT_FRAME = (By.NAME, "atm")
    HEADER_FRAME = (By.NAME, "header")
    BOTTOM_FRAME = (By.NAME, "bottom")
    MENU_ACCOUNT_INFORMATION = (
        By.CSS_SELECTOR, "a[href='account_information_menu.htm']")
    SUBMENU_BALANCE_INQUIRY = (
        By.CSS_SELECTOR, "a[onclick*='balanceinquiry.do']")
    SUBMENU_ACCOUNT_STATEMENT = (
        By.CSS_SELECTOR, "a[onclick*='accountstmt.do']")
    MENU_LOGOUT = (
        By.CSS_SELECTOR, "a[href*='value(actions)=logout']")
    MENU_BACK_TO_HOME = (By.CSS_SELECTOR, "a[href='menu_bar.jsp']")
    MENU_TRANSACTION_HISTORY = (
        By.CSS_SELECTOR, "a[onclick*='value(actions)=history']")


class BalanceLocators(object):
    pass


class AcctStatementLocators(object):
    INPUT_START_DATE = (By.ID, "startDt")
    INPUT_START_MONTH = (By.ID, "startMt")
    INPUT_START_YEAR = (By.ID, "startYr")
    INPUT_END_DATE = (By.ID, "endDt")
    INPUT_END_MONTH = (By.ID, "endMt")
    INPUT_END_YEAR = (By.ID, "endYr")
    SUBMIT_BUTTON = (By.NAME, "value(submit1)")
    DOWNLOAD_BUTTON = (By.NAME, "value(submit2)")


class TransactionHistoryLocators(object):
    INPUT_SELECT_PERIOD = (By.ID, "periode")
    INPUT_START_DATE = (By.ID, "startDt")
    INPUT_START_MONTH = (By.ID, "startMt")
    INPUT_START_YEAR = (By.ID, "startYr")
    INPUT_END_DATE = (By.ID, "endDt")
    INPUT_END_MONTH = (By.ID, "endMt")
    INPUT_END_YEAR = (By.ID, "endYr")
    SUBMIT_BUTTON = (By.NAME, "value(submit)")
