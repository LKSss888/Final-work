📦 Delivery Autotests
Автоматизированные тесты для проекта Delivery, включающие:
UI-тесты с использованием Selenium WebDriver
API-тесты с авторизацией через OAuth 2.0
Отчётность через Allure
Гибкую структуру проекта с поддержкой конфигурации и масштабирования.

Структура проекта:
project/
│
├── tests/                  # Тесты
│   ├── test_ui.py          # UI тесты
│   ├── test_api.py         # API тесты
│   └── conftest.py         # фикстуры и хуки
│
├── pages/                  # Page Object для UI
│   ├── base_page.py
│   ├── login_page.py
│   └── ...
│
├── utils/                  # Вспомогательные утилиты
│   ├── auth.py             # Получение OAuth токена
│
├── data/                   # Конфигурация и данные
│   ├── config.py
│
├── config/                 # Настройки проекта
│   ├── settings.py
│
├── .env                    # Переменные окружения (client_id, client_secret)
├── requirements.txt        # Зависимости
├── pytest.ini              # Настройки Pytest
├── README.md               # Документация
└── .gitignore              # Исключения для Git

🚀 Установка и запуск
1. Установка зависимостей
pip install -r requirements.txt
2. Настройка .env
3. Запуск UI тестов
pytest -m ui --alluredir=allure-results
4. Запуск API тестов
pytest -m api --alluredir=allure-results

### Запуск мок‑API тестов
Если нет доступа к реальному API, можно запустить тесты с мок‑ответами:
pytest -m api_mock --alluredir=allure-results


📊 Генерация Allure отчёта
После запуска тестов:
allure serve allure-results

🔐 Авторизация в API
Для доступа к API используется OAuth 2.0:
Токен автоматически запрашивается при запуске тестов.
Хранится в переменной AUTH_TOKEN.
Передаётся в заголовке каждого запроса: Authorization: Bearer <token>.

⚠️ Обработка капчи
В UI-тестах при обнаружении капчи — пауза 15 секунд для ручного ввода.
В API-тестах — тест автоматически пропускается.

🧪 Маркировка тестов
В pytest.ini настроены маркеры:
[pytest]
markers =
    ui: UI тесты
    api: API тесты
Запуск по маркеру:
pytest -m ui
pytest -m api

📌 Примечания
Все конфиденциальные данные вынесены в .env.
Скриншоты UI-тестов автоматически прикрепляются в Allure при падении.
Код оформлен по PEP8 и структурирован для масштабирования.