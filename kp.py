
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/")
p1=driver.find_elements(By.TAG_NAME,"a")
# here we are collecting multiple objects having same tagname using find_elements
print(p1)
print(len(p1))
for i in range(len(p1)):
    print(p1[i].text)


