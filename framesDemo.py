from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#driver=webdriver.Chrome()





options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

#driver=webdriver.Firefox()
driver.implicitly_wait(5)
#driver=webdriver.Edge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

