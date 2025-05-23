import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(5)
#driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.implicitly_wait(2)
driver.get("http://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
action.context_click(driver.find_element(By.LINK_TEXT,'Top')).perform()
time.sleep(5)
