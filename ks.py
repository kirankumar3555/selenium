# how to handle frames in a webpage
# generally a page might consists of different frames and each frame might consist of a html code
# frames in a webpage starts with an iframe tag or frame tag
# so we need to handle that iframe by using switch to frame concept in webdriver
# so we tell our webdriver to switch it's execution to iframe from main browser
# so after we finishing our work we can use command default_content so that our webdriver switches back to
# default main webpage
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
driver.find_element(By.ID,"datepicker").click()
driver.switch_to.default_content() # to make webdriver get back to main webpage frame

time.sleep(10)
driver.quit()


