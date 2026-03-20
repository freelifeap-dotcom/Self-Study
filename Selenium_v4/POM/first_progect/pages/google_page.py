from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# Пишем (BasePage) в скобках — это значит "наследуем все его умения"
class GoogleSearch(BasePage):
    URL = "https://www.google.com"

    # ЛОКАТОРЫ (наши коробочки-адреса)
    # Пишем их в начале, чтобы если на сайте сменится ID, поменять только здесь
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.aajZCb .gNO89b')

    def open(self):
        self.open_url(self.URL)

    # ДЕЙСТВИЕ: Написать текст
    def enter_words(self, word):
        # Используем метод find_element, который мы написали в BasePage!
        # Звездочка * "распаковывает" кортеж (By.NAME, "q")
        search_field = self.find_clickable_element(self.SEARCH_FIELD)
        search_field.send_keys(word)

    # ДЕЙСТВИЕ: Нажать на поиск
    def click_search(self):
        self.find_clickable_element(self.SEARCH_BUTTON).click()