import requests
import os

AUTH_URL = "https://api.partner.market.yandex.ru/security/oauth/token"

def get_auth_token():
    payload = {
        "client_id": os.getenv("YANDEX_CLIENT_ID"),
        "client_secret": os.getenv("YANDEX_CLIENT_SECRET"),
        "grant_type": "client_credentials",
        "scope": "read write"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(AUTH_URL, data=payload, headers=headers)
    response.raise_for_status()
    token = response.json().get("access_token")
    if not token:
        raise RuntimeError("Не удалось получить токен авторизации")
    return token
