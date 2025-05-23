from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#driver=webdriver.Chrome()


driver=webdriver.Firefox()
driver.implicitly_wait(5)
#driver=webdriver.Edge()

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,'Click Here').click()
openedWindow=driver.window_handles
driver.switch_to.window(openedWindow[1])
msg=driver.find_element(By.CSS_SELECTOR,".example").text
print(msg)
driver.close()
driver.switch_to.window(openedWindow[0])
driver.close()

