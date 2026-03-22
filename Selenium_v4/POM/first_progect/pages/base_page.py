from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # 1. СТРОИМ ОБЪЕКТ (__init__)
    # Когда мы создаем страницу, мы "вручаем" ей драйвер (браузер).
    # self — это способ страницы сказать: "Это МОЙ драйвер".
    def __init__(self, driver):
        self.driver = driver

    # 2. УЧИМ СТРАНИЦУ ИСКАТЬ (find_element)
    # Вместо того чтобы каждый раз писать длинную строку с WebDriverWait,
    # мы создаем один короткий метод.
    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"❌ Не смог найти элемент {locator} на странице {self.driver.current_url}"
        )

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"❌ Не смог найти элемент {locator} на странице {self.driver.current_url}"
        )

    # 3. УЧИМ СТРАНИЦУ ОТКРЫВАТЬСЯ
    def open_url(self, url):
        self.driver.get(url)
