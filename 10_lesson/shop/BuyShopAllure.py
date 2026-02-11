from selenium.webdriver.common.by import By
import allure
class BuyShop:
    def __init__(self, driver):
        self.driver = driver
        """
        Конструктор класса BuyShop.

        :param driver: WebDriver — объект драйвера Selenium.
        """

    @allure.step("Заполнение формы информации о покупателе")
    def buying(self, name, surname, index):
        """
        Заполнение формы информации о покупателе.
        
         """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(surname)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(index)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Проверка итоговой суммы")
    def total_check(self) ->str:
        """
        Возвращает итоговую сумму товаров в корзине
        Тип возвращаемых данных - str
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
