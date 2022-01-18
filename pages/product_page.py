from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), 'Button "Add to cart" not presented'

    def add_to_cart(self):
        add_book = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_book.click()

    def name_of_book(self):
        self.is_element_present(*ProductPageLocators.NAME_OF_BOOK_IN_CART), 'Name of book in cart not presented'
        name_of_book_in_cart = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_CART).text
        assert self.is_element_present(*ProductPageLocators.CHECK_NAME_OF_BOOK), 'Name of book in main not presented'
        name_of_book_in_main = self.browser.find_element(*ProductPageLocators.CHECK_NAME_OF_BOOK).text
        print(name_of_book_in_cart, name_of_book_in_main)
        assert name_of_book_in_cart == name_of_book_in_main, 'Another item added to cart'

    def value_of_cart(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE), 'Price of book in cart not presented'
        value_price_of_product_in_cart = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert self.is_element_present(*ProductPageLocators.CHECK_BASKET_VALUE), 'Price of book in main not presented'
        value_price_of_product_in_main = self.browser.find_element(*ProductPageLocators.CHECK_BASKET_VALUE).text
        print(value_price_of_product_in_cart, value_price_of_product_in_main)
        assert value_price_of_product_in_cart == value_price_of_product_in_main, 'Another price added to cart'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
