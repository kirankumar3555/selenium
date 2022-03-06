
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






