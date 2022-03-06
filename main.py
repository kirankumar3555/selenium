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
# we can use the webdriver_manager to open a browser rather than using chrimedriver exe file
s=Service("drivers/chromedriver.exe")
driver=webdriver.Chrome(service=s)
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
# How to handle checkboxes in selenium python
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
    if p2[i].is_displayed():
        print(p2[i].text)


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
# generally the webdriver is launching webbrowser in minimised window to
# launch it in maximised window we use this below command
driver.maximize_window()
driver.get("https://bing.com")

p1=driver.find_elements(By.TAG_NAME,"a")
for i in range(len(p1)):
    if p1[i].is_displayed():
        print(p1[i].text)
        p1[i].send_keys(Keys.TAB) # keys. command will list down all the keyboard commands
        # if we enter keys. we can see all the keyboard commands listing down

time.sleep(20)
driver.quit()

# here we are trying to select the date after clicking text box
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
f=driver.find_element(By.CLASS_NAME,"demo-frame") # finding the element in the frame using it's frame classname
# so we are storing the information of the frame in f variable
driver.switch_to.frame(f) # webdriver switches it's execution to respective frame
# driver .switch_to.frame(0) # we can find the frame using the index also
# driver.find_element(By.ID,"datepicker").send_keys("02/28/2022")
# here we are sending the text of date in the text box
driver.find_element(By.ID,"datepicker").click()
driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
# finding the element next button using xpath
driver.find_element(By.LINK_TEXT,"31").click()
# we should use link_text for tagnames starting with a and if we want to perform click operation over that


time.sleep(20)
driver.quit()

# how to handle drag and drop
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()
time.sleep(8)
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
obj=driver.find_element(By.ID,"draggable")
ActionChains(driver).drag_and_drop_by_offset(obj,50,50).perform()
# when we don't know where to drop our source in dragging we use daga dn drop by offset
# otherwise we use only dag and drop
#.perform is to perform that operation

driver.quit()

# how to get the size of the draggable object and how to get the desired attribute of the
# object
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
obj=driver.find_element(By.ID,"draggable")
s=obj.size # this gives the height and weight of the object
print(s)
l=obj.location # this gives the x and y coordinate of the object
print(l)
print(obj.get_attribute("class")) # we are getting the class attribute of that object

# when we don't know where to drop our source in dragging we use daga dn drop by offset
# otherwise we use only dag and drop
#.perform is to perform that operation

driver.quit()


# here we are trying to resize the size of resizable clipboard

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/resizable/")
time.sleep(8)
driver.maximize_window()
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
obj=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-e']")
ActionChains(driver).drag_and_drop_by_offset(obj,150,150).perform()

# when we don't know where to drop our source in dragging we use daga dn drop by offset
# otherwise we use only dag and drop
#.perform is to perform that operation

driver.quit()

# here we are trying to drag the window and drop it to the desired drop location

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/droppable/")
time.sleep(5)
f=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(f)
# here we are identifying the draggable object
src=driver.find_element(By.ID,"draggable")
# here we are identifying the droppable object
dest=driver.find_element(By.ID,"droppable")
ActionChains(driver).drag_and_drop(src,dest).perform()

driver.quit()

# here we are trying to get the tooltip of an object

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/tooltip/")
time.sleep(5)
s=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(s)
d=driver.find_element(By.XPATH,"//input[@id='age']") # finding the tooltip object
print(d.get_attribute("title")) # printing the tooltip title
driver.quit()

# how to capture auto search suggestions in a browser

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://bing.com")

driver.find_element(By.ID,"sb_form_q").send_keys("mahendra")
# typing this word in the searchbox
time.sleep(5)
# capturing all the auto search suggestions
c=driver.find_elements(By.XPATH,"//li[@class='sa_sg']")
for i in range(len(c)):
    if c[i].is_displayed():
        print(c[i].text)
# capturing the screenshot and storing in the respective loaction
driver.get_screenshot_as_file("C:/Users/kumar/Downloads/screen/scree.png")
driver.quit()


# mouse hover operation in emirates website
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.emirates.com/in/english/book/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='call-to-action__multiline-wrapper header-popup__btn-content']").click()
obj=driver.find_element(By.XPATH,"//li[@span='second-level-menu__list-item tabs__active-tab']")
ActionChains(driver).move_to_element(obj).perform()
time.sleep(8)
driver.quit()
# if we want to specifically click on a tab on displayed links we might have same xpath for each of them
# so we use (xpath)[count] to choose a specific tab and use click method over that
# so (xpath)[count].click()

# multiple window handling
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://bing.com")
driver.find_element(By.ID,"sb_form_q").send_keys("twitter login")
driver.find_element(By.ID,"search_icon").click()
driver.find_element(By.XPATH,"//li[@class='b_algo']//a").click()
driver.find_element(By.XPATH,"//div[@role='button' and @class='css-18t94o4 css-1dbjc4n r-14lw9ot r-1ets6dv r-sdzlij r-1phboty r-rs99b7 r-eu3ka r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-1ipicw7']//span/span").click()
time.sleep(10)
first=driver.window_handles[0] # saving the first window in the first variable
second=driver.window_handles[1] # saving the second window in the second variable
driver.switch_to_window(second) # telling our driver to shift to second window
driver.switch_to_default_content() # to again get back to main window
time.sleep(9)
driver.quit()

# how to print the text of table rows in html
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-team/india/2/stats")
# printing the player table first 3 names
a = "//tr["
b = "]/td[1]/a"
for i in range(1, 4):
    obj = driver.find_element(By.XPATH, a + str(i) + b)
    print(obj.text)

time.sleep(9)
driver.quit()
# printing the matches of the first 3 names
# a="//tr["
# b="]/td[2]"
# for i in range(1,4):
# obj=driver.find_element(By.XPATH,a+str(i)+b)
# print(obj.text)
# printing the name and no of matches of respective name at a time
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Webdrivers/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-team/india/2/stats")
# printing the player table first 3 names
a = "//tr["
b = "]/td[1]/a"
c = "//tr["
d = "]/td[2]"

for i in range(1, 4):
    obj = driver.find_element(By.XPATH, a + str(i) + b)
    print(obj.text)
    obj_1 = driver.find_element(By.XPATH, c + str(i) + d)
    print(obj_1.text)

time.sleep(9)
driver.quit()
# printing the matches of the first 3 names
# a="//tr["
# b="]/td[2]"
# for i in range(1,4):
# obj=driver.find_element(By.XPATH,a+str(i)+b)
# print(obj.text)

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
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(10) # we are waiting for 15 seconds for the alert to get displayed
a=driver.switch_to.alert # webdriver to switch to alert
print(a.text) # it gets the text from the alert
print("successfully handled the alerts")
#a.send_keys("data") # sends the data in to the alert
#a.accept() # clicks on ok on the alert
#a.dismiss() # clicks on cancel on the alert


time.sleep(15)
driver.quit()

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
print("successfully handled the alerts")
#a.send_keys("data") # sends the data in to the alert
#a.accept() # clicks on ok on the alert
#a.dismiss() # clicks on cancel on the alert


time.sleep(15)
driver.quit()

# handling alerts
# alerts are blocking in nature until we handle them we can't perform any operation on the browser
import pandas as pd
import xlrd
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

loc=("C:/Users/kumar/OneDrive/Desktop/selenium/Book_1.xlsx")
wb=xlrd.open_workbook(loc) # opening the workbook(contains all the sheets of excel)
sheet=wb.sheet_by_index(0) # taking a specific sheet using index
p1=sheet.cell(1,0).value # taking a specific value of a cell inside an excel sheet
print(p1)
print(sheet.nrows) # printing the no of rows in that sheet
print(sheet.ncols) # printing the no of columns in that sheet
for i in range(sheet.nrows): # printing all the row values inside the excel sheet
    p2=sheet.cell(i,0).value
    print(p2)

import unittest


class MyTestCase(unittest.TestCase):
    def test_addNumbers(self):
        print(2+3)
        self.assertEqual(2,2) # we can add assertions for every unit test script
        #self.assertEqual(2,12)
    def test_subNumbers(self):
        print(5-1)
# we should always use test_ before every method name inside the methods of unittest class.
#if __name__ == '__main__':
    #unittest.main()


import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self): # set up gets executed before every test case inside testcase class
        print("set up gets executed before every test case inside testcase class")
    def tearDown(self): #teardown method gets executed after every test case inside testcase class
        print("teardown method gets executed after every test case inside testcase class")
    def test_add(self):
        print(5+3)
    def test_sub(self):
        print(8-2)



import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # set upclass gets executed only once in the entire test case methods before testcase methods execution
        print(" set upclass gets executed only once in the entire test case methods before testcase methods execution")
    @classmethod
    def tearDownClass(cls): # teardownclass gets executed only once in the entire test case methods after testcase methods execution
        print("teardownclass gets executed only once in the entire test case methods after testcase methods execution")
    def test_add(self):
        print(5+3)
    def test_sub(self):
        print(8-2)

# Where we use these setUpclass and tearDownclass in automation world?
# We use them in unit testing which is illustrated below in this case.
# in this program we are creating a unittest case where we are signing into a gmail account
# using setUp class and performing the test case methods and logging off using tearDown class.


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # opening of the browser and maximising is set up in setup class
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.google.com/intl/en-GB/gmail/about/")
        cls.driver.maximize_window()
    # test case methods are executed in their method name alphabetical order
    # here test_a_gmaillogin gets executed first and next test_b_password executes
    def test_a_gmaillogin(self): # test case for gmaillogin # test_a is executed first
        self.driver.find_element(By.XPATH,"//a[@data-action='sign in']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("kumar.kiran744@gmail.com")
        self.driver.find_element(By.XPATH,"//span[@class='VfPpkd-vQzf8d']").click()
        time.sleep(5)
    def test_b_password(self): # test case for entering password
        self.driver.find_element(By.XPATH,"//div[@class='Xb9hP]/input").send_keys("Kiran@391")
        time.sleep(10)
    @classmethod
    def tearDownClass(cls): #teardown class for closing browser
        time.sleep(15)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

# Where we use these setUpclass and tearDownclass in automation world?
# We use them in unit testing which is illustrated below in this case.
# in this program we are creating a unittest case where we are signing into a gmail account
# using setUp class and performing the test case methods and logging off using tearDown class.
# the next important in testing is reporting the test case execution results. There are two methods
# in reporting. One is htmltestrunner and other is Pycharm self report generation.
# for htmltestrunner we need to import HtmlTestRunner and we need to add
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/kumar/PycharmProjects/jj/UnitTest/report'),verbosity=2)

import HtmlTestRunner
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # opening of the browser and maximising is set up in setup class
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.google.com/intl/en-GB/gmail/about/")
        cls.driver.maximize_window()
    def test_a_gmaillogin(self): # test case for gmaillogin
        self.driver.find_element(By.XPATH,"//a[@data-action='sign in']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("kumar.kiran744@gmail.com")
        self.driver.find_element(By.XPATH,"//span[@class='VfPpkd-vQzf8d']").click()
        time.sleep(5)
    def test_b_password(self): # test case for entering password
        self.driver.find_element(By.XPATH,"//div[@class='Xb9hP]/input").send_keys("Kiran@391")
        time.sleep(10)
    @classmethod
    def tearDownClass(cls): #teardown class for closing browser
        time.sleep(15)
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/kumar/PycharmProjects/jj/UnitTest/report'),verbosity=2)


# This is page object model. First we created a PageObjectModel directory and then Pages, Tests directory
# inside of PageObjectModel
# then we created a Pagesfile.py in Pages directory
# then we created a loginTest.py file in Tests directory
# the advantage of using the pageobjectmodel is if we want to change or replace an element in the
# script and if it is present in 50 areas of the script and in different classes
# it is difficult to change in every area manually so instead if
# we pass that into a variable then it will be easy.
class loginPage(): # this class is in Pagesfile.py
    #here we are using a variable to store xpath of a specific elements in the class
    # and using them in the test script.
    signin_text_filed_XPATH="//a[@data-action='sign in']"
    username_text_field_XPATH="//input[@type='email']"
    nextbutton_text_filed_XPATH="//span[@class='VfPpkd-vQzf8d']"

# Where we use these setUpclass and tearDownclass in automation world?
# We use them in unit testing which is illustrated below in this case.
# in this program we are creating a unittest case where we are signing into a gmail account
# using setUp class and performing the test case methods and logging off using tearDown class.
# the next important in testing is reporting the test case execution results. There are two methods
# in reporting. One is htmltestrunner and other is Pycharm self report generation.
# for htmltestrunner we need to import HtmlTestRunner and we need to add
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/kumar/PycharmProjects/jj/UnitTest/report'),verbosity=2)


# this is the example for the pageobject model. # we are using the page class variables inside this script
import HtmlTestRunner
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObjectModel.Pages.Pagesfile import loginPage

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # opening of the browser and maximising is set up in setup class
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.google.com/intl/en-GB/gmail/about/")
        cls.driver.maximize_window()
    def test_a_gmaillogin(self): # test case for gmaillogin
        loginprop=loginPage()
        self.driver.find_element(By.XPATH,"//a[@data-action='sign in']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,loginprop.username_text_field_XPATH).send_keys("kumar.kiran744@gmail.com")
        self.driver.find_element(By.XPATH,loginprop.nextbutton_text_filed_XPATH).click()
        time.sleep(5)
    #def test_b_password(self): # test case for entering password
        #self.driver.find_element(By.XPATH,"//div[@class='Xb9hP]/input").send_keys("Kiran@391")
        #time.sleep(10)
    @classmethod
    def tearDownClass(cls): #teardown class for closing browser
        time.sleep(15)
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/kumar/PycharmProjects/jj/UnitTest/report'),verbosity=2)

# page factory model is an extention of page object model.
# in page factory model we use page properties as well as methods
# the difference b/w pageobjectmodel and pagefactory model is the include both page properties as well
# as methods.
# we can use those methods inside our test cases to use those methods and execute the test cases.
from selenium.webdriver.common.by import By


class loginPage(): # this class is in Pagesfile.py
    #here we are using a variable to store xpath of a specific elements in the class
    # and using them in the test script.
    signin_text_filed_XPATH="//a[@data-action='sign in']"
    username_text_field_XPATH="//input[@type='email']"
    nextbutton_text_filed_XPATH="//span[@class='VfPpkd-vQzf8d']"

    def login(self,username):
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("username")









































