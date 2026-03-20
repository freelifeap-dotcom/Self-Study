import time
from pages.google_page import GoogleSearch

def test_google_search(browser):
    # 1. Запускаем браузер

    google_page = GoogleSearch(browser)

    google_page.open()
    google_page.enter_words("Погода на завтра")
    google_page.click_search()

    time.sleep(3)

# Вызываем функцию, чтобы она сработала:
# test_google_search()