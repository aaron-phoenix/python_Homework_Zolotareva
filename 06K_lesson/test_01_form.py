from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

def test_form():

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    submit = driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary")
    submit.click()

    element = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    actual_color = element.value_of_css_property("background-color")
    assert actual_color == "rgba(248, 215, 218, 1)"

    list = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']

    for id in list:
        element = driver.find_element(By.ID, id)
        back_color = element.value_of_css_property("background-color")
        assert back_color == "rgba(209, 231, 221, 1)" 

    driver.quit()