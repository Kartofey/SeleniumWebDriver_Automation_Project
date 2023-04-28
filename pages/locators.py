from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    CATALOGUE_LINK = (By.CSS_SELECTOR, ".dropdown-menu:nth-child()")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".icon-ok-sign")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class CataloguePageLocators():
    THE_SHELCODERS_HANDBOOK = (By.CSS_SELECTOR, '[title="he shellcoder\'s handbook"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")