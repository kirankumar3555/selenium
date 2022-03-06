# here in this file we are dealing with checkboxes
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65&id=language_section#language-section")
# here we are cliclking on the checkbox of settings in bing website
#driver.find_element(By.ID,"enAS").click()
# lets check whether the checkbox is ticked if not lets print something else
p1=driver.find_element(By.ID,"enAS").is_selected()
print(p1)
if p1==True:
    print("already ticked")
else:
    driver.find_element(By.ID,"enAS").click()
    print("now ticked")

time.sleep(10)
driver.quit()
