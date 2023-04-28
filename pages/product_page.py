from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_click_add_to_cart(self):
        button_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_link.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Basket button is not presented"

    def get_success_message_with_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME)

    def should_be_same_product_name(self):
        success_message = self.get_success_message_with_product_name().text
        actual_product_name = self.get_product_name().text
        assert actual_product_name in success_message, f"Expected success message to contain {actual_product_name}, but got {success_message}"

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

    def get_cart_price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.CART_PRICE)

    def should_be_same_product_price(self):
        cart_price = self.get_cart_price_of_product().text
        product_price = self.get_product_price().text
        assert cart_price == product_price, f"The price in the cart{cart_price} and the price of the product{product_price} on the page are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is not disappeared, but should be"
