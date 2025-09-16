from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class SearchPage(BasePage):
    FIRST_PRODUCT = (By.CLASS_NAME, "product-item")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(text(), 'Добавить')]")
    CART_BADGE = (By.CLASS_NAME, "cart-badge")
    
    @allure.step("Добавление первого товара в корзину")
    def add_first_product_to_cart(self):
        first_product = self.find_element(self.FIRST_PRODUCT)
        add_button = first_product.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()
    
    @allure.step("Проверка что товар в корзине")
    def is_product_in_cart(self):
        return self.is_visible(self.CART_BADGE)