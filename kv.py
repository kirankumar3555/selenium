# how to handle drag and drop
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()
time.sleep(8)
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
obj=driver.find_element(By.ID,"draggable")
ActionChains(driver).drag_and_drop_by_offset(obj,50,50).perform()
# when we don't know where to drop our source in dragging we use daga dn drop by offset
# otherwise we use only dag and drop
#.perform is to perform that operation

driver.quit()


