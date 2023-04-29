from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time
import random

# Имитация того, что гость видит элемент для перехода на страницу авторизации из страницы с продуктом
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# Имитация того, что гость может перейти на страницу авторизации из сраницы продукта
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# Имитация того, что гость добавляет продукт в корзину (тестируется с разными промо ссылками)
# @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "pytest.param('7', marks=pytest.mark.xfail)", "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_same_product_name()
    page.should_be_same_product_price()

# Имитация того, что гость видит сообщение об успешном добавлении товара в корзину
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_to_cart()
    page.should_not_be_success_message()

# Имитация того, что гость не видит сообщение об успешном добавлении товара в козину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# Имитация того, что гость видит, как сообщение об успешном добавлении товара в козину исчезло
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_to_cart()
    page.should_be_disappear_success_message()

# Имитация того, что гость не видит продукт на странице корзины, открытой из страницы продукта
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_about_empty_basket()

# Имитация того, что гость не видит сообщения о пустой корзине на странице корзины, открытой из страницы продукта
@pytest.mark.xfail
def test_guest_cant_see_message_about_empty_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_message_about_empty_basket()

# Имитация того, что гость видит, что сообщение о пустой корзине на странице корзины, открытой из страницы продукта исчезло
@pytest.mark.xfail
def test_message_about_empty_basket_disappeared_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_disappear_message_about_empty_basket()

# Класс имитирует, что пользователь регестрируется и может добавить продукт в корзину и не видит сообщение об успешном добавлении, если он ничего не добавлял
@pytest.mark.basket
class TestUserAddToBasketFromProductPage():

# Фикстура открывает страницу авторизации, заполняет форму регестрации и проверяет, что после нажатия на кнопу пользователь зарегестрирован
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = int(''.join(map(str, random.sample(range(10), 9))))
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

# Имитация того, что пользователь может добавить продукт в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_click_add_to_cart()
        page.should_be_same_product_name()
        page.should_be_same_product_price()

# Имитация того, что пользователь не может увидеть сообщение об успешно добавленном товаре
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()