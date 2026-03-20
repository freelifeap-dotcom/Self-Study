from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EbaySearch(BasePage):
    URL_EBAY = "https://www.ebay.com"
    SEARCH_FIELD = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.ID, 'gh-search-btn')
    FIRST_RESULT = (By.CSS_SELECTOR, 'ul.srp-results>li.s-card:first-child div[role="heading"]')

    def open(self):
        self.open_url(self.URL_EBAY)

    def search_item(self, item_name):
        search_field = self.find_clickable_element(self.SEARCH_FIELD)
        search_field.send_keys(item_name)

    def click_search(self):
        self.find_clickable_element(self.SEARCH_BUTTON).click()

    def get_first_result_text(self):
        return self.find_element(self.FIRST_RESULT).text
