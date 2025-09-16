from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class RestaurantPage(BasePage):
    SORT_BUTTON = (By.XPATH, "//span[contains(text(), 'Сортировка')]")
    SORT_MODAL = (By.XPATH, "//div[contains(text(), 'Какие показать сначала?')]")
    
    @allure.step("Открытие модального окна сортировки")
    def open_sorting_modal(self):
        self.click(self.SORT_BUTTON)
    
    @allure.step("Проверка видимости модального окна сортировки")
    def is_sorting_modal_visible(self):
        return self.is_visible(self.SORT_MODAL)