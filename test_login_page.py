from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# Имитация входа гостя на страницу авторизации из стартовой страницы и проверка, что это именно та страница
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# Имитация того, что гость может увидеть верный url страницы авторизации, перейдя на неё
def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()

# Имитация того, что гость может увидеть форму авторизации перейдя на страницу авторизации
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()

# Имитация того, что гость может увидеть форму регистрации перейдя на страницу авторизации
def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()