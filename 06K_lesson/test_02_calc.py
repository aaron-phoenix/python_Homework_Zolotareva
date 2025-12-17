from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_calc():

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    input = driver.find_element(By.CSS_SELECTOR, "#delay")
    input.clear()
    input.send_keys("45")

    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][text()='7']").click()
    driver.find_element(By.XPATH, "//span[contains(@class, 'operator')][text()='+']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'][text()='8']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning'][text()='=']").click()

    waiter = WebDriverWait(driver, 50)

    waiter.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"),
            "15"
        )
    )
    result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
    result = result_element.text

    assert result == "15"

    driver.quit()
