from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

def test_shop():
    waiter = WebDriverWait(driver, 5)
    waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    waiter = WebDriverWait(driver, 5)
    waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    waiter = WebDriverWait(driver, 5)
    waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Elena")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Zolotareva")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("394074")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    waiter = WebDriverWait(driver, 5)
    waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert total == "Total: $58.29"

    driver.quit()