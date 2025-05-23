import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(2)
#driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.get("http://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Saurav Dandapat')
driver.find_element(By.NAME, "email").send_keys("Hello@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")

dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)


driver.find_element(By.ID, "exampleCheck1").click()

# //tagname[@attribute='value'] -> //input[@type='submit']
# tagname[attribute='value']  -->  input[type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
Success_Message=driver.find_element(By.CLASS_NAME, "alert-success").text
# alert alert-success alert-dismissible
time.sleep(2)
print(Success_Message)

assert 'Success' in Success_Message

title=driver.title
print(title)
driver.close()
driver.quit()