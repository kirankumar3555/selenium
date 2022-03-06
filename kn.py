# here in this file we are dealing with radio buttons
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65&id=language_section#language-section")
# here we are clicking on the strict radio button of settings in bing website
#driver.find_element(By.ID,"enAS").click()
driver.find_element(By.ID,"adlt_set_strict").click()
p1=driver.find_element(By.ID,"adlt_set_strict").is_selected()
# if strict radio button is selected then it return true
print(p1)


time.sleep(10)
driver.quit()
