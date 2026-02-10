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
    def authorisation(self):
        """
        Вводим логин и пароль в форму авторизации на сайте магазина.
        
        :param CSS_SELECTOR: локаторы для формы авторизации и нажатия кнопки войти из DevTools
        :param send_keys: логин и пароль для формы авторизации
        """
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Ожидание результата")
    def waits(self):
        """
        Ожидает загрузки страницы после авторизации
        Ожидаемый результат - загрузка html-тега body
        :param: int
        :param CSS_SELECTOR: локатор тега body из DevTools
        
        """
        waiter = WebDriverWait(self.driver, 5)

        waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )
