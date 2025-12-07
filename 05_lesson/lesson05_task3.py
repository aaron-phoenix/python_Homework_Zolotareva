from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")

search_field = "input"
search_field = driver.find_element(By.CSS_SELECTOR, search_field)

search_field.send_keys("Sky")
sleep(3)

search_field.clear()
sleep(3)

search_field.send_keys("Pro")
sleep(3)

driver.quit()
