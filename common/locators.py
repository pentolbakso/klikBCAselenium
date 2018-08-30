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
