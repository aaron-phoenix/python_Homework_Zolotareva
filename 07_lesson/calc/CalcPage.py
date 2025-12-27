from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver

    def open_calc(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def operation(self):
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'operator')][text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning'][text()='=']").click()
        
    def time(self, seconds):
        time_waiter = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        time_waiter.clear()
        time_waiter.send_keys(seconds)
    
    def result(self):
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        res = result_element.text
        assert int(res) == 15
    
    def waits(self):
        waiter = WebDriverWait(self.driver, 50)

        waiter.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"),
            "15"
        )
    )