import requests
import allure
from config.settings import settings

class APIClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.session = requests.Session()
    
    @allure.step("Отправка POST запроса к {endpoint}")
    def post(self, endpoint, json_data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        default_headers = {
            "Content-Type": "application/json",
            "User-Agent": "AutoTests/1.0"
        }
        if headers:
            default_headers.update(headers)
        
        response = self.session.post(
            url, 
            json=json_data, 
            headers=default_headers,
            timeout=settings.API_TIMEOUT
        )
        return response