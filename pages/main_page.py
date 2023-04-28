from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def go_to_catalogue_page(self):
        catalogue_link = self.browser.find_element(*MainPageLocators.CATALOGUE_LINK)
        catalogue_link.click()

    def should_be_catalogue_link(self):
        assert self.is_element_present(*MainPageLocators.CATALOGUE_LINK), "Catalogue link is not presented"
        