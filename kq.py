
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://developer.salesforce.com/signup")
#p1=driver.find_elements(By.TAG_NAME,"option")
# to get all the values in the drop down
#print(p1)
#for i in range(len(p1)):
    #print(p1[i].text)
p1=driver.find_element(By.ID,"option")
p2=p1.find_elements(By.TAG_NAME,"option")
for i in range(len(p2)):
    print(p2[i].text)





