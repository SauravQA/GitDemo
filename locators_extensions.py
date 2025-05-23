import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(2)
#driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.get("http://rahulshettyacademy.com/client/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys('demo@gmail.com')
driver.find_element(By.ID, "userPassword").send_keys('password@123')
driver.find_element(By.ID, "confirmPassword").send_keys('password@123')
driver.find_element(By.XPATH, "//button[@type='submit']").click()
title=driver.title
print(title)
time.sleep(5)



