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