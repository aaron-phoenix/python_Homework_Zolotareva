from selenium import webdriver
import pytest
from shop.AuthShop import AuthShop
from shop.BuyShop import BuyShop
from shop.CartShop import CartShop
from shop.MainShop import MainShop

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_shop(driver):
    auth = AuthShop(driver)
    main = MainShop(driver)
    cart = CartShop(driver)
    buy = BuyShop(driver)
    auth.open_shop()
    auth.authorisation()
    auth.waits()
    main.add_items()
    main.add_cart()
    auth.waits()
    cart.checkout()
    auth.waits()
    buy.buying()
    auth.waits()
    buy.result("Total: $58.29")
