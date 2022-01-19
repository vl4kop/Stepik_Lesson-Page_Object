from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_empty_cart(self):
        """Метод проверяет отсутствуют ли в корзине товары (отрицательная проверка)"""
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_CART), 'Cart not empty'

    def should_be_empty_cart(self):
        """Метод проверяет пустая ли корзина"""
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART), 'Cart not empty'
