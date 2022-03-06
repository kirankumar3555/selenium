# here we are trying to get the tooltip of an object

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/tooltip/")
time.sleep(5)
s=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(s)
d=driver.find_element(By.XPATH,"//input[@id='age']") # finding the tooltip object
print(d.get_attribute("title")) # printing the tooltip title
driver.quit()


