# Lets' talk about waits:
# Suppose if we are creating a test script for clicking a search button, which goes to the next page
# then if we didn't give these synchronisation commands like time.sleep()
# our script would not be able to recognise or find the corresponding object
# in the next page because it take sometime to go to next page and our find_element command
# gives an exception error. So inorder to avoid that we use wait commands.
# there are two kinds of waits in the webdriver.
# 1) Implicit wait
# 2) Explicit wait
# 1) In implicit wait, the wait commands (synchronisation commands) are used at the top of the test
# script such that it will be applicable for all the commands in the script. So it gives time for the
# object in the next page to load and if the object is not loaded within the specified wait, then it throws a not found
# element exception.
# When we are switching between different pages we go for these waits
# 2) Explicit wait, this is used for a specific object in the webpage. If an object takes sometime
# to load in a webpage we use this explicit wait.

#Implicit wait is for the entire webpage whereas explicit wait is for a specific element in the webpage.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-team/india/2/stats")
driver.implicitly_wait(30)
table=driver.find_element(By.XPATH,"//table[@class='table table-responsive cb-series-stats']/tbody")
trlist=table.find_elements(By.TAG_NAME,"tr")
WebDriverWait(driver,10).until(expected_conditions.element_to_be_selected) #explicit wait
# we need to import expected_conditions for explicit wait
a="//tr["
b="]/td[1]/a"
for i in range(1,len(trlist)+1):
    obj=driver.find_element(By.XPATH,a+str(i)+b)
    print(obj.text)


time.sleep(8)
driver.quit()
