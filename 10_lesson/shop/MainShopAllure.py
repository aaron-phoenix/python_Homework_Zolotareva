from selenium.webdriver.common.by import By
import allure

class MainShop:
    def __init__(self, driver):
        self.driver = driver
        """
        Конструктор класса MainShop.

        :param driver: WebDriver — объект драйвера Selenium.
        """
    @allure.step("Добавление товаров в корзину")
    def add_items(self):
        """
        Нажатие кнопки Add to cart
        
        :param CSS_SELECTOR: локаторы кнопок add to cart из DevTools
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    @allure.step("Открытие корзины")
    def add_cart(self):
        """
        Открывает корзину с ее содержимым по клику на иконку корзины.
        
        :param CSS_SELECTOR: локатор для иконки корзины из DevTools
        """
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()