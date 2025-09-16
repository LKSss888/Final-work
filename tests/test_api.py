import pytest
import requests
import allure
from data.config import BASE_URL, get_auth_headers


@allure.feature("API Поиск и Расписание")
@pytest.mark.api
class TestAPITestCases:

    @allure.story("Поиск товара на кириллице")
    def test_search_cyrillic(self):
        headers = get_auth_headers()
        url = f"{BASE_URL}/v1/search"
        payload = {
            "text": "суши",
            "location": {"longitude": 46.02028, "latitude": 51.60379}
        }
        response = requests.post(url, json=payload, headers=headers)
        self._check_captcha(response)
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        assert "items" in response.json(), "В ответе нет ключа 'items'"

    @allure.story("Поиск товара на латинице")
    def test_search_latin(self):
        headers = get_auth_headers()
        url = f"{BASE_URL}/v1/search"
        payload = {
            "text": "sushi",
            "location": {"longitude": 46.02028, "latitude": 51.60379}
        }
        response = requests.post(url, json=payload, headers=headers)
        self._check_captcha(response)
        assert response.status_code == 200
        assert "items" in response.json()

    @allure.story("Поиск с пустым запросом")
    def test_search_empty(self):
        headers = get_auth_headers()
        url = f"{BASE_URL}/v1/search"
        payload = {
            "text": "",
            "location": {"longitude": 46.02028, "latitude": 51.60379}
        }
        response = requests.post(url, json=payload, headers=headers)
        self._check_captcha(response)
        assert response.status_code == 200
        assert "items" in response.json()

    @allure.story("Поиск со спецсимволами")
    def test_search_special_characters(self):
        headers = get_auth_headers()
        url = f"{BASE_URL}/v1/search"
        payload = {
            "text": "!@#$%^&*()",
            "location": {"longitude": 46.02028, "latitude": 51.60379}
        }
        response = requests.post(url, json=payload, headers=headers)
        self._check_captcha(response)
        assert response.status_code == 200
        assert "items" in response.json()

    @allure.story("Получение расписания доставки")
    def test_get_schedule(self):
        headers = get_auth_headers()
        url = f"{BASE_URL}/v1/schedule"
        response = requests.get(url, headers=headers)
        self._check_captcha(response)
        assert response.status_code == 200
        assert "deliverySlots" in response.json()

    # Вспомогательный метод для обработки капчи
    def _check_captcha(self, response):
        if "captcha" in response.text.lower():
            pytest.skip("Обнаружена капча, тест пропущен")
