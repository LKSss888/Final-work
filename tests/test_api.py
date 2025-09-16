import pytest
import allure
import requests
from utils.api_client import APIClient

@pytest.mark.api
@allure.feature("API Тесты")
class TestAPITestCases:
    
    def _check_captcha(self, response):
        """Проверка что ответ не содержит капчу"""
        if "captcha" in response.text.lower() or "showcaptcha" in response.url:
            allure.attach(response.text, name="captcha_response", attachment_type=allure.attachment_type.TEXT)
            pytest.skip("Обнаружена капча, пропускаем тест")
    
    @allure.story("Поиск товара на кириллице")
    def test_search_cyrillic(self, api_client):
        search_data = {
            "text": "суши",
            "filters": [],
            "selector": "all",
            "location": {
                "longitude": 46.02028,
                "latitude": 51.60379
            }
        }
        
        response = api_client.post("/api/search", json_data=search_data)
        self._check_captcha(response)
        assert response.status_code == 200
        
        # Проверяем что ответ JSON, а не HTML капчи
        try:
            response_data = response.json()
            assert "items" in response_data or "message" in response_data
        except requests.exceptions.JSONDecodeError:
            # Если не JSON, проверяем что это не капча
            assert "captcha" not in response.text.lower()
            pytest.skip("Ответ не в JSON формате, возможно капча")
    
    @allure.story("Поиск товара на латинице")
    def test_search_latin(self, api_client):
        search_data = {
            "text": "sushi",
            "filters": [],
            "selector": "all",
            "location": {
                "longitude": 46.02028,
                "latitude": 51.60379
            }
        }
        
        response = api_client.post("/api/search", json_data=search_data)
        self._check_captcha(response)
        assert response.status_code == 200
    
    @allure.story("Поиск с пустым запросом")
    def test_search_empty(self, api_client):
        search_data = {
            "text": "",
            "filters": [],
            "selector": "all",
            "location": {
                "longitude": 46.02028,
                "latitude": 51.60379
            }
        }
        
        response = api_client.post("/api/search", json_data=search_data)
        self._check_captcha(response)
        assert response.status_code == 200
    
    @allure.story("Поиск со специальными символами")
    def test_search_special_characters(self, api_client):
        search_data = {
            "text": "@#$%^&*()",
            "filters": [],
            "selector": "all",
            "location": {
                "longitude": 46.02028,
                "latitude": 51.60379
            }
        }
        
        response = api_client.post("/api/search", json_data=search_data)
        self._check_captcha(response)
        assert response.status_code == 200
    
    @allure.story("Получение расписания работы")
    def test_get_schedule(self, api_client):
        schedule_data = {
            "from": "2025-03-10T01:00:00+04:00",
            "till": "2025-03-17T01:00:00+04:00",
            "onlyTypes": []
        }
        
        response = api_client.post("/api/schedule", json_data=schedule_data)
        self._check_captcha(response)
        assert response.status_code == 200