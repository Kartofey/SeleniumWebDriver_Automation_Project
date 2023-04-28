from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# def test_guest_should_see_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_login_url()      # выполняем метод страницы — переходим на страницу логина

# def test_guest_should_see_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_login_form()      # выполняем метод страницы — переходим на страницу логина

# def test_guest_should_see_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_register_form()      # выполняем метод страницы — переходим на страницу логина