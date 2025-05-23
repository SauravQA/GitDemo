import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expectedList=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList=[]
driver=webdriver.Chrome()
#driver.implicitly_wait(2)
#driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.implicitly_wait(2)
driver.get("http://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
time.sleep(2)


results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,'div/button').click()

assert actualList==expectedList

driver.find_element(By.CSS_SELECTOR,'img[alt="Cart"]').click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Total price Validation

prices=driver.find_elements(By.XPATH,"//tr/td[5]/p")
total_Price =0

for price in prices:
    total_Price= total_Price + int(price.text)

print (total_Price)
total_amnt = driver.find_element(By.CSS_SELECTOR,".totAmt")

assert int(total_amnt.text)== total_Price



driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys('rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promo_msg=driver.find_element(By.CSS_SELECTOR,'.promoInfo').text
assert 'Code applied' in promo_msg

discountedPrice=float(driver.find_element(By.CSS_SELECTOR,'.discountAmt').text)

assert discountedPrice< total_Price