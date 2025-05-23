import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(2)
#driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.get("http:yatra.com")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"(//p[normalize-space()='DEL, Indira Gandhi International'])[1]").click()
driver.find_element(By.CLASS_NAME,"MuiInput-input").send_keys('bhu')
time.sleep(2)
departure_city_List= driver.find_elements(By.XPATH,"//div[contains(@class,'fw-600')]")
# //input[@id='input-with-icon-adornment'] /// .MuiBox-root.css-offmes
print(len(departure_city_List))

for city in departure_city_List:
    print('bhubaneswar')
    if city == 'Bhubaneswar, (BBI)':
        city.click()
        print('bhubaneswar')
        break


time.sleep(15)

