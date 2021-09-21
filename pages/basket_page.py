import time
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        time.sleep(3)
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), "There are items"

    def should_be_message_empty_basket(self):
        time.sleep(3)
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No message that basket is empty"
