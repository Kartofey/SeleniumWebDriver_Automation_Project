from .base_page import BasePage
from .locators import BasketPageLocators

# Класс методов для страницы корзины
class BasketPage(BasePage):

# Проверка наличия сообщения, что корзина пуста
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No empty basket message"

# Проверка отсутсвия сообщения, что корзина пуста
    def should_not_be_message_about_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
       "Success message is presented, but should not be"

# Проверка исчезания сообщения, что корзина пуста
    def should_be_disappear_message_about_empty_basket(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
       "Success message is not disappeared, but should be"