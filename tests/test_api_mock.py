import pytest
import allure
import json

@pytest.mark.api
@allure.feature("API Тесты (Mock)")
class TestAPIMockTestCases:
    
    @allure.story("Поиск товара на кириллице - Mock")
    def test_search_cyrillic_mock(self):
        """Mock тест поиска на кириллице"""
        with allure.step("Имитация успешного ответа API"):
            mock_response = {
                "items": [
                    {"id": 1, "name": "Суши Филадельфия", "price": 350, "weight": 250},
                    {"id": 2, "name": "Суши Калифорния", "price": 320, "weight": 220}
                ],
                "total": 2,
                "status": "success"
            }
            
            assert mock_response["status"] == "success"
            assert len(mock_response["items"]) > 0
            assert any("суши" in item["name"].lower() for item in mock_response["items"])
    
    @allure.story("Поиск товара на латинице - Mock")
    def test_search_latin_mock(self):
        """Mock тест поиска на латинице"""
        with allure.step("Имитация успешного ответа API"):
            mock_response = {
                "items": [
                    {"id": 3, "name": "Sushi Set", "price": 500, "weight": 300},
                    {"id": 4, "name": "Sushi Box", "price": 450, "weight": 280}
                ],
                "total": 2,
                "status": "success"
            }
            
            assert mock_response["status"] == "success"
            assert len(mock_response["items"]) > 0
    
    @allure.story("Поиск с пустым запросом - Mock")
    def test_search_empty_mock(self):
        """Mock тест пустого поиска"""
        with allure.step("Имитация ответа для пустого запроса"):
            mock_response = {
                "frequently_searched": ["суши", "пицца", "бургеры", "роллы"],
                "popular_categories": ["Японская кухня", "Пицца", "Бургеры"],
                "status": "success"
            }
            
            assert mock_response["status"] == "success"
            assert "frequently_searched" in mock_response
    
    @allure.story("Поиск со специальными символами - Mock")
    def test_search_special_chars_mock(self):
        """Mock тест спецсимволов"""
        with allure.step("Имитация ответа для некорректного запроса"):
            mock_response = {
                "message": "По вашему запросу ничего не найдено",
                "suggestions": ["суши", "роллы", "пицца"],
                "status": "success"
            }
            
            assert mock_response["status"] == "success"
            assert "message" in mock_response
    
    @allure.story("Получение расписания работы - Mock")
    def test_get_schedule_mock(self):
        """Mock тест расписания"""
        with allure.step("Имитация ответа с расписанием"):
            mock_response = {
                "schedule": {
                    "monday": {"open": "09:00", "close": "22:00"},
                    "tuesday": {"open": "09:00", "close": "22:00"},
                    "wednesday": {"open": "09:00", "close": "22:00"},
                    "thursday": {"open": "09:00", "close": "22:00"},
                    "friday": {"open": "09:00", "close": "23:00"},
                    "saturday": {"open": "10:00", "close": "23:00"},
                    "sunday": {"open": "10:00", "close": "22:00"}
                },
                "status": "success"
            }
            
            assert mock_response["status"] == "success"
            assert "schedule" in mock_response