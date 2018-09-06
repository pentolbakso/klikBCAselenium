from page.base_page import BasePage
from common.locators import TransactionHistoryLocators
from selenium.webdriver.support.ui import Select


class TransactionHistoryPage(BasePage):

    def verifyPage(self):
        return "HISTORY TRANSAKSI" in self.driver.page_source

    def getHistory(self):
        # change periode
        radios = self.driver.find_elements(
            *TransactionHistoryLocators.INPUT_SELECT_PERIOD)
        for radio in radios:
            if radio.get_attribute("value") == "1":
                radio.click()
                break

        months = ("Januari", "Februari", "Maret", "April", "Mei", "Juni",
                  "Juli", "Agustus", "September", "Oktober", "November", "Desember")

        # get 1 month statements from now
        startMt = Select(self.getElement(
            TransactionHistoryLocators.INPUT_START_MONTH))
        current_month = months.index(
            startMt.first_selected_option.get_attribute("value"))
        if current_month == 0:
            # January, update year input to last year
            startMt.select_by_value("Desember")
            startYr = Select(self.getElement(
                TransactionHistoryLocators.INPUT_START_YEAR))
            current_year = int(
                startYr.first_selected_option.get_attribute("value"))
            startYr.select_by_value(str(current_year - 1))
        else:
            startMt.select_by_value(months[current_month-1])

        self.getElement(TransactionHistoryLocators.SUBMIT_BUTTON).click()

        # should we wait?
        table = self.driver.find_elements_by_tag_name("table")[3]

        result = []
        trs = table.find_elements_by_css_selector("tr[bgcolor]")
        for tr in trs[1:]:  # skip first row
            tds = tr.find_elements_by_css_selector("td[width]")
            # print(tr.get_attribute('innerHTML'))
            amount = tds[3].text.replace("\n", "")
            amount = amount.replace(" ", "")
            result.append({
                'date': tds[0].text,
                'type': tds[1].text,
                'description': tds[2].text,
                'amount': amount,
                'status': tds[4].text
            })
        return result
