from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class MainPage(BasePage):
    USER_AVATAR = (By.CLASS_NAME, "user-avatar")
    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    CART_ICON = (By.CLASS_NAME, "cart-icon")
    
    @allure.step("Проверка что пользователь авторизован")
    def is_user_logged_in(self):
        return self.is_visible(self.USER_AVATAR)
    
    @allure.step("Поиск товара")
    def search_product(self, product_name):
        self.type_text(self.SEARCH_FIELD, product_name)
        self.click(self.SEARCH_BUTTON)