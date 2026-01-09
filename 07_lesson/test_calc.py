from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
    res = result_element.text
    assert int(res) == 15
    