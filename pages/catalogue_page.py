from .base_page import BasePage
from .locators import CataloguePageLocators

class MainPage(BasePage):

    def go_to_product_page(self):
        product_link = self.browser.find_element(*CataloguePageLocators.THE_SHELCODERS_HANDBOOK)
        product_link.click()

    def should_be_product_link(self):
        assert self.is_element_present(*CataloguePageLocators.THE_SHELCODERS_HANDBOOK), "Product link is not presented"