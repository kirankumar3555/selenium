# selenium is the package and webdriver is a component of selenium.
# 4 components of selenium are
#selenium ide,selenium webdriver, selenium rc, selenium grid
# selenium helps us to automate the web browsers and the tasks performed over the web browser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install()) #this can make us to not use exe file to open a browser

...
# here webdriver is a class having chrome as a method
#driver is an instance or an object of the webdriver class

...

driver.get("https://bing.com") # driver.get is opening the website or getting to the page
# locators:it is the heart of the selenium
# in a webpage developers assign a unique property to the objects(text box,link,image,etc)
# as a tester we need to find that unique property of a specific object that we want to test
# webdriver can only identify an object using only three properties. they are
# Id,class,name.
# if an object is not having the above three properties, what we use to identify an object?
# We choose either xpath or css selector to identify that object.
# in real world majorly we use xpath as a default locator for the objects which don't have
# default properties like id,class and name.
# syntax of xpath is //html tagname[@property type='property value] Ex: //label[@for='sb_form_go']
# to know whether our xpath is a valid one
# we use ctrl+f and write our xpath and the search in html code for that object in elements tab
#another way is $x("xpath") in console tab
#fn+F12 to display all the html elements of a webpage
# we can identify the object properties using inspect element,selenium ide and webdriver locator or element locator addon
S=driver.find_element(By.ID,'sb_form_q') # finding the object by id here we are finding the id of
# search box
S.send_keys("msd") # for typing the words we are using send_keys and the text that we want to search for
driver.find_element(By.XPATH,"//label[@for='sb_form_go']").click()  # here since we don't have id,class,name
# we are using xpath to find the search button object
time.sleep(5) # giving some time for the page to display the results
driver.quit() # closing the browser.





