import pytest  
import allure
import sys
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем корневую папку в PYTHONPATH
current_dir = Path(__file__).parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from config.settings import settings

@pytest.fixture(scope="function")
def driver():
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
        
        # Добавляем user-agent чтобы уменьшить шанс капчи
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {settings.BROWSER}")
    
    driver.implicitly_wait(settings.TIMEOUT)
    driver.maximize_window()
    
    # Переходим на сайт
    driver.get(settings.BASE_URL)
    
    # Обработка капчи - просто ждем вместо input()
    if "captcha" in driver.current_url:
        print("⚠️ Обнаружена капча! Ожидание 15 секунд для ручного ввода...")
        time.sleep(15)  # Ждем 15 секунд для ручного ввода
    
    yield driver
    
    if driver:
        driver.quit()

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API клиента"""
    from utils.api_client import APIClient
    return APIClient()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
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
            print(f"Failed to take screenshot: {e}")