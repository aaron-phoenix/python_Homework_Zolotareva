from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthShop:
    def __init__(self, driver):
        self.driver = driver

    def open_shop(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def authorisation(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def waits(self):
        waiter = WebDriverWait(self.driver, 5)

        waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )

    
    