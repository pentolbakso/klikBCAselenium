from page.base_page import BasePage
from common.locators import BalanceLocators


class BalancePage(BasePage):

    def verifyPage(self):
        return "INFORMASI SALDO" in self.driver.page_source

    def getBalance(self):
        table = self.driver.find_elements_by_tag_name("table")[2]

        result = []
        trs = table.find_elements_by_tag_name("tr")
        for tr in trs[1:]:  # skip first row
            tds = tr.find_elements_by_tag_name("td")
            result.append({
                'account': tds[0].text,
                'type': tds[1].text,
                'currency': tds[2].text,
                'amount': tds[3].text
            })
        return result
