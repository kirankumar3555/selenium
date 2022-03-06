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


