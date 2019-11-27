from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_to_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def product_should_match_book(self):
        product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_page.text
        book_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_page.text
        assert product_name == book_name, "Название товара и книги не совпадают!"

    def price_should_match_book(self):
        price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = price_page.text
        book_price_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price_page.text
        assert price == book_price, "Цена товара и книги не совпадают!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't disappeared, but should be"
