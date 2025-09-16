from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class NotificationsPage(BasePage):
    NOTIFICATIONS_BUTTON = (By.XPATH, "//button[@aria-label='Уведомления']")
    NOTIFICATIONS_MODAL = (By.CLASS_NAME, "notifications-modal")
    
    @allure.step("Открытие уведомлений")
    def open_notifications(self):
        self.click(self.NOTIFICATIONS_BUTTON)
    
    @allure.step("Проверка видимости окна уведомлений")
    def is_notifications_visible(self):
        return self.is_visible(self.NOTIFICATIONS_MODAL)