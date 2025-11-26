from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

search_field = "input#username"
search_field = driver.find_element(By.CSS_SELECTOR, search_field)

search_field.send_keys("tomsmith")
search_field = "input#password"

search_field = driver.find_element(By.CSS_SELECTOR, search_field)
search_field.send_keys("SuperSecretPassword!")
sleep(3)

login_button = "button.radius"
login_button = driver.find_element(By.CSS_SELECTOR, login_button).click()
sleep(3)

text = "#flash"
search_text = driver.find_element(By.CSS_SELECTOR, text) 
print(f'Текст с зеленой плашки: {search_text.text}')

driver.quit()
