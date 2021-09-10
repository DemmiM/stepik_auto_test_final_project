from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket =self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        print(product_name,message)
        assert product_name == message, f"{product_name} isn`t {message}"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(product_price,basket_price)
        assert basket_price == product_price, f"{basket_price} is not equal {product_price}"

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()
