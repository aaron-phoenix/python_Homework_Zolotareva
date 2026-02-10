from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class AuthShop:
    def __init__(self, driver):
        self.driver = driver
        """
        Конструктор класса AuthShop.

        :param driver: WebDriver — объект драйвера Selenium.
        """
    @allure.step("Ожидание открытия страницы магазина")
    def open_shop(self):
        self.driver.get("https://www.saucedemo.com/")
        """
        Открывает страницу магазина.
        """
    @allure.step("Авторизация на сайте магазина")
    def authorisation(self, login, password):
        """
        Метод для заполнения формы авторизации на сайте магазина.
        
        :param login: логин пользователя
        :param: пароль пользователя
        """
        
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Ожидание результата")
    def waits(self, time:int = 5):
        """
        Ожидает загрузки страницы после авторизации
        Ожидаемый результат - загрузка html-тега body
        По умолчанию значение параметра 5.
        
        """
        waiter = WebDriverWait(self.driver, time)

        waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )
