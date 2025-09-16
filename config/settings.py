import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = "https://market-delivery.yandex.ru/saratov?shippingType=delivery"
    LOGIN = os.getenv("LOGIN", "elizavetakovalcuk74@gmail.com")
    PASSWORD = os.getenv("PASSWORD", "elizaveta1991!")
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    TIMEOUT = 10
    API_TIMEOUT = 30

settings = Settings()