# here we are trying to resize the size of resizable clipboard

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/resizable/")
time.sleep(8)
driver.maximize_window()
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
obj=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-e']")
ActionChains(driver).drag_and_drop_by_offset(obj,150,150).perform()

# when we don't know where to drop our source in dragging we use daga dn drop by offset
# otherwise we use only dag and drop
#.perform is to perform that operation

driver.quit()


