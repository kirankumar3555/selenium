# how to get the size of the draggable object and how to get the desired attribute of the
# object
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
s=obj.size # this gives the height and weight of the object
print(s)
l=obj.location # this gives the x and y coordinate of the object
print(l)
print(obj.get_attribute("class")) # we are getting the class attribute of that object

# when we don't know where to drop our source in dragging we use daga dn drop by offset
# otherwise we use only dag and drop
#.perform is to perform that operation

driver.quit()


