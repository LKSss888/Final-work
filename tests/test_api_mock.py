import pytest
import requests
import allure
from unittest.mock import patch

BASE_URL = "https://api.partner.market.yandex.ru"


@allure.feature("API Mock — Поиск и Расписание")
@pytest.mark.api_mock
class TestAPIMockCases:

    @allure.story("Поиск товара на кириллице (mock)")
    def test_search_cyrillic_mock(self):
        mock_response = {
            "items": [
                {"id": 1, "name": "Суши сет", "price": 500},
                {"id": 2, "name": "Ролл Филадельфия", "price": 300}
            ]
        }
        with patch("requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = mock_response

            url = f"{BASE_URL}/v1/search"
            payload = {"text": "суши", "location": {"longitude": 46.02, "latitude": 51.60}}
            response = requests.post(url, json=payload)

            assert response.status_code == 200
            assert "items" in response.json()
            assert len(response.json()["items"]) == 2

    @allure.story("Поиск товара на латинице (mock)")
    def test_search_latin_mock(self):
        mock_response = {
            "items": [
                {"id": 3, "name": "Sushi Set", "price": 550}
            ]
        }
        with patch("requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = mock_response

            url = f"{BASE_URL}/v1/search"
            payload = {"text": "sushi", "location": {"longitude": 46.02, "latitude": 51.60}}
            response = requests.post(url, json=payload)

            assert response.status_code == 200
            assert response.json()["items"][0]["name"] == "Sushi Set"

    @allure.story("Поиск с пустым запросом (mock)")
    def test_search_empty_mock(self):
        mock_response = {"items": []}
        with patch("requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = mock_response

            url = f"{BASE_URL}/v1/search"
            payload = {"text": "", "location": {"longitude": 46.02, "latitude": 51.60}}
            response = requests.post(url, json=payload)

            assert response.status_code == 200
            assert response.json()["items"] == []

    @allure.story("Поиск со спецсимволами (mock)")
    def test_search_special_characters_mock(self):
        mock_response = {"items": []}
        with patch("requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = mock_response

            url = f"{BASE_URL}/v1/search"
            payload = {"text": "!@#$%^&*()", "location": {"longitude": 46.02, "latitude": 51.60}}
            response = requests.post(url, json=payload)

            assert response.status_code == 200
            assert response.json()["items"] == []

    @allure.story("Получение расписания доставки (mock)")
    def test_get_schedule_mock(self):
        mock_response = {
            "deliverySlots": [
                {"date": "2025-09-17", "time": "12:00-14:00"},
                {"date": "2025-09-17", "time": "14:00-16:00"}
            ]
        }
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response

            url = f"{BASE_URL}/v1/schedule"
            response = requests.get(url)

            assert response.status_code == 200
            assert "deliverySlots" in response.json()
            assert len(response.json()["deliverySlots"]) == 2
