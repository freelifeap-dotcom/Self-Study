import os
import pytest # нужен чтобы мы могли использовать фикстуры(специальные функции-помощники)
import undetected_chromedriver as uc

# Пишем саму фикстуру
# @pytest.fixture(): Это "декоратор". Он говорит Пайтону: Это не просто функция, это ресурс, который можно выдавать тестам по запросу
@pytest.fixture()
def browser():  # Название нашей фикстуры. Именно это слово нужно писать в скобках у тестов
    # Печатаем в консоль для наглядности
    print('\n[LOG] Подготовка браузера...')

    # Создаем объект драйвера
    driver = uc.Chrome()
    driver.maximize_window()

    # Передаем драйвер в тест
    yield driver    # Это самое важное слово. Оно работает как "пауза"
    # Сначала выполняется все, что ДО yield
    # Затем управление передается в тест (тест выполняется)
    # Когда тecт закончился (успешно или с ошибкой), выполняется всё, что ПОСЛЕ yield

    # Этот код выполнится ПОСЛЕ завершения теста
    print('\n [LOG] Закрытие браузера...')
    driver.quit()

# --- ДОБАВЛЯЮ БЛОК ДЛЯ СКРИНШОТОВ ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Этот хук проверяет результат выполнения теста
    outcome = yield
    rep = outcome.get_result()

    #Если тест упал (failed) во время выполнения (call)
    if rep.when == 'call' and rep.failed:
        try:
            # Создаем папку, если ее нет
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')

            # Очищаем имя теста от символов, которые запрещены в именах файлов Windows
            clean_name = item.name.replace("[", "_").replace("]", "_").replace(":", "_")
            # Берем драйвер из фикстуры 'browser'
            driver = item.funcargs['browser']

            # Формируем имя: название_теста.png
            img_path = os.path.join('screenshots', f"fail_{item.name}.png")
            driver.save_screenshot(img_path)
            # Сохраняем в папку
            print(f"\n[!!!] ТЕСТ УПАЛ. Скриншот сохранен: {img_path}")

            # Сохраняем ЛОГ (тескт ошибки) в файл.txt
            log_path = os.path.join('screenshots', f"fail_{clean_name}.txt")
            with open(log_path, 'w', encoding="utf=8") as f:
                f.write(f"Тест: {item.name}\n")
                f.write(f"URL: {driver.current_url}\n")
                # call.excinfo.value — это и есть текст ошибки из WebDriverWait или assert
                f.write(f"Ошибка: {call.excinfo.value}\n")
            print(f"📄 ЛОГ ОШИБКИ СОХРАНЕН: {log_path}")
        except Exception as e:
            print(f"⚠️ Не удалось сохранить улики: {e}")
