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


