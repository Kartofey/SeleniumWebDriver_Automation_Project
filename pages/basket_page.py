from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Catalogue link is not presented"

    def should_not_be_message_about_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_disappear_message_about_empty_basket(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
       "Success message is not disappeared, but should be"