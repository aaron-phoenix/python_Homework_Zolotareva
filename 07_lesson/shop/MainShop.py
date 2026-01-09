from selenium.webdriver.common.by import By

class MainShop:
    def __init__(self, driver):
        self.driver = driver
    
    def add_items(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    def add_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        