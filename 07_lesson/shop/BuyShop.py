from selenium.webdriver.common.by import By

class BuyShop:
    def __init__(self, driver):
        self.driver = driver
    
    def buying(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Elena")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Zolotareva")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("394074")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def result(self, value):
        total = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        assert total == value