from .base_page import BasePage
from .locators import ProductPageLocators

# Класс методов для страницы выбранного продукта
class ProductPage(BasePage):

# Получение цены продукта, указанной в описании продукта
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

# Получение цены продукта, указанной в корзине
    def get_cart_price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.CART_PRICE)

# Получение имени продукта из сообщения о добавлении его в корзину
    def get_success_message_with_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)

# Получение имени продукта из основного его описания
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME)

# Проверка, что на кнопку "Добавить в корзину" можно нажать
    def should_be_click_add_to_cart(self):
        button_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_link.click()

# Проверка, что элемент кнопка "Добавить в корзину" есть на странице
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

# Сравнение идентичности названия самого продукта с названием продукта добавленного в корзину
    def should_be_same_product_name(self):
        success_message = self.get_success_message_with_product_name().text
        actual_product_name = self.get_product_name().text
        assert actual_product_name in success_message, f"Expected success message to contain {actual_product_name}, but got {success_message}"

# Сравнение идентичности цены самого продукта с ценой указанной в корзине
    def should_be_same_product_price(self):
        cart_price = self.get_cart_price_of_product().text
        product_price = self.get_product_price().text
        assert cart_price == product_price, f"Expected price in the cart {cart_price} and the price of the product{product_price} on the page are different"

# Проверка, что сообщения об успешном добавлении в корзину нет
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

# Проверка, что сообщения об успешном добавлении в корзину исчезает через время
    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is not disappeared, but should be"
