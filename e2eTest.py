from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
#driver=webdriver.Chrome()
driver.implicitly_wait(2)
#driver=webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
#//a[contains(@href,'shop')]m--Xpath

products=driver.find_elements(By.XPATH,"//app-card/div")
print(products)

for product in products:
   productName = product.find_element(By.XPATH,"div/h4/a").text
   print(productName)
   if productName == "iphone X" :
      product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CLASS_NAME,"checkbox-primary").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
success_msg=driver.find_element(By.CLASS_NAME,"alert-success").text
assert 'Thank you' in success_msg

driver.close()
