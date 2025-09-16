from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class AddressPage(BasePage):
    ADDRESS_BUTTON = (By.XPATH, "//span[contains(text(), 'Ленина')]")
    ADDRESS_MODAL = (By.XPATH, "//div[contains(text(), 'Куда доставить?')]")
    
    @allure.step("Открытие модального окна адреса")
    def open_address_modal(self):
        self.click(self.ADDRESS_BUTTON)
    
    @allure.step("Проверка видимости модального окна адреса")
    def is_address_modal_visible(self):
        return self.is_visible(self.ADDRESS_MODAL)