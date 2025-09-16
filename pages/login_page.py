from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
import time

class LoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//*[contains(text(), 'Войти')]")
    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "passwd")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    @allure.step("Проверка видимости кнопки входа")
    def is_login_button_visible(self):
        return self.is_visible(self.LOGIN_BUTTON)
    
    @allure.step("Авторизация пользователя")
    def login(self, username, password):
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)
        self.type_text(self.LOGIN_FIELD, username)
        self.click(self.SUBMIT_BUTTON)
        time.sleep(2)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        time.sleep(3)