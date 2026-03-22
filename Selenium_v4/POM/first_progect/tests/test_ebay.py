import time
import undetected_chromedriver as uc
from pages.ebay_page import EbaySearch
def test_ebay_search(browser):

    ebay_page = EbaySearch(browser)

    ebay_page.open()
    ebay_page.search_item("iPhone 15")
    ebay_page.click_search()
    result_text = ebay_page.get_first_result_text()
    assert "iPhone" in result_text, f"❌ Ожидали iPhone в результатах, но получили:'{result_text[:50]}...'"
    print(f"Тест пройден! Нашелся товар: {result_text}")


    time.sleep(2)