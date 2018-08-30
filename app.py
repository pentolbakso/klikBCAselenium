from selenium import webdriver
from page.login_page import LoginPage
from config import USERID, PASSWORD

driver = webdriver.Chrome()

login_page = LoginPage(driver)
login_page.launchUrl("https://ibank.klikbca.com")
if login_page.verifyPage == False:
    print("Loading login page failed! is site running?")
    exit(1)

login_page.fillUserID(USERID)
login_page.fillPassword(PASSWORD)
main_page = login_page.clickLoginButton()
if main_page.verifyPage() == False:
    print("Login failed? check your UserID/Password")
    exit(1)

print("Login success")

balance_page = main_page.clickMenuBalanceInquiry()
balances = balance_page.getBalance()

print("\nBalance Inquiry result:")
for balance in balances:
    print("{account:15s} {type:10s} {currency:5s} {amount:s}".format(**balance))

# driver.close()
