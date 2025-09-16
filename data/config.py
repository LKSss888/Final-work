import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.partner.market.yandex.ru"

def get_auth_headers():
    from utils.auth import get_auth_token
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
