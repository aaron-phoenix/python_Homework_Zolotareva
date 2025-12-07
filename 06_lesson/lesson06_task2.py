from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

search_field = "#newButtonName"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
waiter = WebDriverWait(driver, 15, 0.5)
waiter.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()
