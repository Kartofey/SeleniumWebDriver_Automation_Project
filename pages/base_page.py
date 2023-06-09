from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
import math

# Родительский класс базовых методов
class BasePage():

# Конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

# Запуск драйвера
    def open(self):
        self.browser.get(self.url)

# Переход на страницу авторизации
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

# Переход на страницу корзины
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

# Проверка наличия элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

# Проверка, что элемент не появляется на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

# Проверка, что элемент исчезает со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

# Проверка, что ссылка на страницу авторизации существует
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

# Проверка, что ссылка на страницу корзины существует
    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"

# Проверка, что пользователь авторизирован или прошел регистрацию
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
        " probably unauthorised user"

# Метод вводит нужный код в alert, подтверждает и вводит промо код для книги
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
