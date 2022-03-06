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

import PageObjectModel.Pages.Pagesfile
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
        g=PageObjectModel.Pages.Pagesfile.loginPage()
        g.login("kumar.kiran744@gmail.com")
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
