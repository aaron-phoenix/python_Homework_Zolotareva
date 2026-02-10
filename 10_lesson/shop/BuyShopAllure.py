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
    def buying(self):
        """
        Заполнение формы информации о покупателе.
        
        :param CSS_SELECTOR: локаторы для полей формы информации о покупателе из DevTools и кнопки continue
        """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Elena")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Zolotareva")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("394074")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Проверка итоговой суммы")
    def total_check(self):
        """
        Возвращает итоговую сумму товаров в корзине
        :params CSS_SELECTOR: локатор отображения итоговой суммы товаров из DevTools
        Тип возвращаемых данных - str
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
