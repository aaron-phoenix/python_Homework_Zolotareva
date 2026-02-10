from selenium.webdriver.common.by import By
import allure
class CartShop:
    def __init__(self, driver):
        self.driver = driver
        """
        Конструктор класса CartShop.

        :param driver: WebDriver — объект драйвера Selenium.
        """

    @allure.step("Открытие формы информации о покупателе")
    def checkout(self):
        """
        Открывает форму заполнения информации о покупателе
        
        :param CSS_SELECTOR: локатор для кнопки checkout из DevTools
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()