from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from shop.AuthShopAllure import AuthShop
from shop.BuyShopAllure import BuyShop
from shop.CartShopAllure import CartShop
from shop.MainShopAllure import MainShop
import allure

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.title("Тестирование интернет-магазина товаров")
@allure.description("Тестирование проверяет авторизацию, добавление товаров в корзину, заполнение информации о покупателе и отображение итоговой суммы в корзине интернет-магазина.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Интернет-магазин")
def test_shop(driver):
    """
    Тест проверяет основные бизнесс-функции интернет-магазина
    
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param CSS_SELECTOR: локатор для отображения итоговой суммы из DevTools
    :param total: str
    """
    auth = AuthShop(driver)
    main = MainShop(driver)
    cart = CartShop(driver)
    buy = BuyShop(driver)
    login = "standard_user"
    password = "secret_sauce"
    name = "Elena"
    surname = "Zolotareva"
    index = "394074"
    with allure.step("Ожидание открытия страницы магазина"):
        auth.open_shop()
    with allure.step("Авторизация на сайте магазина"):
        auth.authorisation(login, password)
    with allure.step("Ожидание результата"):
        auth.waits()
    with allure.step("Добавление товаров в корзину"):
        main.add_items()
    with allure.step("Открытие корзины"):
        main.add_cart()
    with allure.step("Ожидание результата"):
        auth.waits()
    with allure.step("Открытие формы информации о покупателе"):
        cart.checkout()
    with allure.step("Ожидание результата"):
        auth.waits()
    with allure.step("Заполнение формы информации о покупателе"):
        buy.buying(name, surname, index)
    with allure.step("Ожидание результата"):
        auth.waits()

    with allure.step("Проверка итоговой суммы"):
        buy.total_check()
        assert buy.total_check() == "Total: $58.29"
