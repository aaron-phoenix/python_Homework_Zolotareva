from selenium import webdriver
from calc.CalcPage import CalcPage
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calc(driver):
    calcPage = CalcPage(driver)
    calcPage.open_calc()
    calcPage.time("45")
    calcPage.operation()
    calcPage.waits()
    calcPage.result()