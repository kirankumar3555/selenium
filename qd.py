#printing the name and no of matches of respective name at a time
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-team/india/2/stats")
# printing the player table first 3 names
a="//tr["
b="]/td[1]/a"
c="//tr["
d="]/td[2]"

for i in range(1,4):
    obj=driver.find_element(By.XPATH,a+str(i)+b)
    print(obj.text)
    obj_1=driver.find_element(By.XPATH,c+str(i)+d)
    print(obj_1.text)

time.sleep(9)
driver.quit()
# printing the matches of the first 3 names
#a="//tr["
#b="]/td[2]"
#for i in range(1,4):
    #obj=driver.find_element(By.XPATH,a+str(i)+b)
    #print(obj.text)



