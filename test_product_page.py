from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
import random

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "pytest.param('7', marks=pytest.mark.xfail)", "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_click_add_to_cart()
#     page.solve_quiz_and_get_code()
#     page.should_be_same_product_name()
#     page.should_be_same_product_price()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_click_add_to_cart()
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()

# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_click_add_to_cart()
#     page.should_be_disappear_success_message()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_message_about_empty_basket()

# @pytest.mark.xfail
# def test_guest_cant_see_message_about_empty_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_not_be_message_about_empty_basket()

# @pytest.mark.xfail
# def test_message_about_empty_basket_disappeared_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_disappear_message_about_empty_basket()

@pytest.mark.basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = int(''.join(map(str, random.sample(range(10), 9))))
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_click_add_to_cart()
        page.should_be_same_product_name()
        page.should_be_same_product_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()