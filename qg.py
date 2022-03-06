# handling alerts
# alerts are blocking in nature until we handle them we can't perform any operation on the browser
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
f=driver.find_element(By.NAME,"iframeResult")
driver.switch_to.frame(f)
driver.find_element(By.XPATH,"//html/body/button").click()
time.sleep(2) # we are waiting for 15 seconds for the alert to get displayed
a=driver.switch_to.alert # webdriver to switch to alert
print(a.text) # it gets the text from the alert
a.accept()
print("successfully handled the alerts")

#a.send_keys("data") # sends the data in to the alert
#a.accept() # clicks on ok on the alert
#a.dismiss() # clicks on cancel on the alert


time.sleep(15)
driver.quit()





