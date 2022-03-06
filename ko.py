# here in this file we are dealing with dropdown buttons
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65&id=language_section#language-section")
#driver.find_element(By.ID,"rpp").send_keys("10") #changing the dropdown values using send_keys
#another way is to use select
dd=driver.find_element(By.ID,"rpp")
s=Select(dd)
# s.select_by_index(2) # selecting the values with it's index or order
#(indexing starts with 0 )
# s.select_by_value("10") # selecting the values with it's value
# s.select_by_visible_text("Auto") # selecting the values in dropdown based on text visible
c1=s.options # options is a command which captures all the element's values in the dropdown and
# stores in a variable
# now let's print value of each elements
for element in c1:
    c2=element.get_attribute("value")
    print(c2)


time.sleep(10)
driver.quit()
