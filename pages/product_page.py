from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_to_cart(self):
        """Метод который проверяет наличие кнопки 'добавить в корзину'"""
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), 'Button "Add to cart" not presented'

    def add_to_cart(self):
        """Метод который добавляет в корзину товар"""
        add_book = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_book.click()

    def name_of_book(self):
        """Метод проверяет соответствует ли название добавленного товара названию в корзине"""
        self.is_element_present(*ProductPageLocators.NAME_OF_BOOK_IN_CART), 'Name of book in cart not presented'
        name_of_book_in_cart = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_CART).text
        assert self.is_element_present(*ProductPageLocators.CHECK_NAME_OF_BOOK), 'Name of book in main not presented'
        name_of_book_in_main = self.browser.find_element(*ProductPageLocators.CHECK_NAME_OF_BOOK).text
        # print(name_of_book_in_cart, name_of_book_in_main)
        assert name_of_book_in_cart == name_of_book_in_main, 'Another item added to cart'

    def value_of_cart(self):
        """Метод проверяет соответствует ли цена добавленного товара цене корзины"""
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE), 'Price of book in cart not presented'
        value_price_of_product_in_cart = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert self.is_element_present(*ProductPageLocators.CHECK_BASKET_VALUE), 'Price of book in main not presented'
        value_price_of_product_in_main = self.browser.find_element(*ProductPageLocators.CHECK_BASKET_VALUE).text
        # print(value_price_of_product_in_cart, value_price_of_product_in_main)
        assert value_price_of_product_in_cart == value_price_of_product_in_main, 'Another price added to cart'

    def should_not_be_success_message(self):
        """Метод который проверяет отсутствие сообщения о добавление в корзину (отрицательная проверка)"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        """Метод который проверяет что элемент исчезает с течением времени"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
