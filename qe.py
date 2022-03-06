#dynamic handiling of webtables (printing all the names in the rows of a table)
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-team/india/2/stats")
table=driver.find_element(By.XPATH,"//table[@class='table table-responsive cb-series-stats']/tbody")
trlist=table.find_elements(By.TAG_NAME,"tr")
print(len(trlist))
# printing the player table first 3 names
a="//tr["
b="]/td[1]/a"


for i in range(1,len(trlist)+1):
    obj=driver.find_element(By.XPATH,a+str(i)+b)
    print(obj.text)

time.sleep(9)
driver.quit()
# printing the matches of the first 3 names
#a="//tr["
#b="]/td[2]"
#for i in range(1,4):
    #obj=driver.find_element(By.XPATH,a+str(i)+b)
    #print(obj.text)



