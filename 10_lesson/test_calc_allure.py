from selenium import webdriver
from selenium.webdriver.common.by import By
from calc.CalcPageAllure import CalcPage
import pytest
import allure

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора: 7+8=15")
@allure.description("Тестирование проверяет работоспособность калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Калькулятор")
def test_calc(driver):
    """Тест проверяет работу калькулятора с различными операциями.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param delay: int — задержка в секундах для выполнения операции.
    :param res: int - ожидаемый результат
    """
    calcPage = CalcPage(driver)
    with allure.step("Открытие страницы калькулятора"):
        calcPage.open_calc()
    with allure.step("Установка времени задержки delay"):
        calcPage.time("45")
    with allure.step("Поиск и нажатие кнопок калькулятора"):
        calcPage.operation()
    with allure.step("Ожидание результата"):
        calcPage.waits()
    with allure.step("Получение и проверка результата теста"):
        assert calcPage.result() == '15'