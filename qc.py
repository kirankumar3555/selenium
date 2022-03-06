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
driver.switch_to_default_content() # to again get back to main window or use driver.switch_to_default_content(first)
time.sleep(9)
driver.quit()

