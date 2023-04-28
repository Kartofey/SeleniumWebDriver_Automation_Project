from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest
import time

# Имитация входа гостя на страницу авторизации из стартовой страницы
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

# Имитация того, что гость видит элемент для перехода на страницу авторизации
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# Имитация того, что гость перешел на страницу корзины и видит сообщение о пустой корзине
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    time.sleep(30)
    basket_page.should_be_message_about_empty_basket()

# Имитация того, что гость перешел на страницу корзины и не видит сооющения, что корзина пуста
@pytest.mark.xfail
def test_guest_cant_see_message_about_empty_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_message_about_empty_basket()

# Имитация того, что гость перешел на страницу корзины и сообщение, что корзина пуста, исчезает через время
@pytest.mark.xfail
def test_message_about_empty_basket_disappeared_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_disappear_message_about_empty_basket()
