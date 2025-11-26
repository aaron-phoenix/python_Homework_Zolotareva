from selenium import webdriver
driver = webdriver.Chrome()
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

button = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
search_box = driver.find_element(By.XPATH, button).click()

sleep(10)
