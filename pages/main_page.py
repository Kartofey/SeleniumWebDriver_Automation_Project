from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

# Класс методов для стартовой страницы
class MainPage(BasePage):

# Метод для перехода на страницу каталога книг
    def go_to_catalogue_page(self):
        catalogue_link = self.browser.find_element(*MainPageLocators.CATALOGUE_LINK)
        catalogue_link.click()

# Проверка наличия ссылки на страницу каталога
    def should_be_catalogue_link(self):
        assert self.is_element_present(*MainPageLocators.CATALOGUE_LINK), "Catalogue link is not presented"
        