from page.base_page import BasePage
from common.locators import AcctStatementLocators
from selenium.webdriver.support.ui import Select


class AccountStatementPage(BasePage):

    def verifyPage(self):
        return "MUTASI REKENING" in self.driver.page_source

    def getStatements(self):
        # get 1 month statements from now
        startMt = Select(self.getElement(
            AcctStatementLocators.INPUT_START_MONTH))
        current_month = int(
            startMt.first_selected_option.get_attribute("value"))
        if current_month == 1:
            # January, update year input to last year
            startMt.select_by_value("12")
            startYr = Select(self.getElement(
                AcctStatementLocators.INPUT_START_YEAR))
            current_year = int(
                startYr.first_selected_option.get_attribute("value"))
            startYr.select_by_value(str(current_year - 1))
        else:
            startMt.select_by_value(str(current_month - 1))

        self.getElement(AcctStatementLocators.SUBMIT_BUTTON).click()

        # should we wait?
        table = self.driver.find_elements_by_tag_name("table")[4]

        result = []
        trs = table.find_elements_by_tag_name("tr")
        for tr in trs[1:]:  # skip first row
            tds = tr.find_elements_by_tag_name("td")
            desc = tds[1].text.replace("\n", " ")
            result.append({
                'date': tds[0].text,
                'description': desc,
                'cab': tds[2].text,
                'amount': tds[3].text,
                'type': tds[4].text,
                'balance': tds[5].text
            })
        return result
