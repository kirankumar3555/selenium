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



