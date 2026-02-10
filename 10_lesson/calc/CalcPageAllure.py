from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
    """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
    
    @allure.step("Открытие страницы калькулятора")
    def open_calc(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        """
        Открывает страницу калькулятора.
        """
        self.driver.maximize_window()
        """
        Разворачивает окно браузера на весь экран.
        """
    @allure.step("Поиск и нажатие кнопок калькулятора")
    def operation(self):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: локаторы - XPATH кнопок калькулятора,
        полученные с помощью DevTools.
        """
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'operator')][text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning'][text()='=']").click()
        
    @allure.step("Установка времени задержки delay")
    def time(self, seconds):
        """
        Устанавливает время задержки получения результата
        в поле по локатору #delay,
        предварительно очистив поле.
        :param seconds: int
        """
        time_waiter = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        time_waiter.clear()
        time_waiter.send_keys(seconds)
    
    @allure.step("Ожидание результата")
    def waits(self):
        """
        Ожидает появление результата вычислений на экране калькулятора.
        Ожидаемый результат - введенный параметр.
        :param: str
        Добавляем +1 секунду ко времени ожидания
        """
        waiter = WebDriverWait(self.driver, 50)

        waiter.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"),
            "15"
        )
    )
    @allure.step("Получение и проверка результата теста")
    def result(self):
        """
        Возвращает результат вычислений
        Тип возвращаемых данных - str
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
    