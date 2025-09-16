import pytest
import allure
import sys
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Добавляем корневую папку в PYTHONPATH
current_dir = Path(__file__).parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from config.settings import settings
from utils.auth import get_auth_token


# ---------------- UI FIXTURE ---------------- #
@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска браузера"""
    if settings.BROWSER.lower() == "chrome":
        options = Options()

        if settings.HEADLESS:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # User-Agent для снижения вероятности капчи
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )

        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {settings.BROWSER}")

    driver.implicitly_wait(settings.TIMEOUT)
    driver.maximize_window()

    # Переходим на сайт
    driver.get(settings.BASE_URL)

    # Обработка капчи — пауза для ручного ввода
    if "captcha" in driver.current_url:
        print("⚠️ Обнаружена капча! Ожидание 15 секунд для ручного ввода...")
        time.sleep(15)

    yield driver

    if driver:
        driver.quit()


# ---------------- API FIXTURE ---------------- #
@pytest.fixture(scope="session")
def auth_headers():
    """Фикстура для авторизованных заголовков API"""
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


# ---------------- AUTO-SKIP API TESTS ---------------- #
def pytest_collection_modifyitems(config, items):
    """
    Автоматически скипаем только реальные API-тесты (маркер 'api'),
    если нет client_id и client_secret.
    Мок-тесты (маркер 'api_mock') выполняются всегда.
    """
    api_access = bool(os.getenv("YANDEX_CLIENT_ID") and os.getenv("YANDEX_CLIENT_SECRET"))
    if not api_access:
        skip_marker = pytest.mark.skip(reason="Нет client_id и client_secret — реальные API недоступны")
        for item in items:
            if "api" in item.keywords and "api_mock" not in item.keywords:
                item.add_marker(skip_marker)


# ---------------- SCREENSHOT ON FAIL ---------------- #
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении UI-тестов"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")
