from selenium import webdriver
driver = webdriver.Chrome()
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

button = "button.btn-primary"
search_box = driver.find_element(By.CSS_SELECTOR, button).click()


sleep(10)
