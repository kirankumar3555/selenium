# here we are trying to drag the window and drop it to the desired drop location

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/droppable/")
time.sleep(5)
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
# here we are identifying the draggable object
src=driver.find_element(By.ID,"draggable")
# here we are identifying the droppable object
dest=driver.find_element(By.ID,"droppable")
ActionChains(driver).drag_and_drop(src,dest).perform()

driver.quit()


