#there are 4 robotic sections inside a robotic file
#first section is
# *** settings ***
#*** variables ***
#*** test cases ***
#*** keywords ***
# we can also but each one of these sections in separate file.
# all the libraries are to be installed under settings section

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      https://www.flipkart.com/
${browser}  chrome

*** Test Cases ***
LoginTest         # this is a testcase name
    #create webdriver    chrome  executable_path="C:\Webdrivers\chromedriver\chromedriver.exe"
    # we can create a webdriver by using the driver path or else
    # we can copy the chrome webdriver in the python>scripts and add that path into
    #environmental variables path
    #open browser    https://www.flipkart.com/   chrome  # here open browser is a keyword
    open browser    ${url}   ${browser}
    logintoapplication      # we can use this user defined keyword inside the testcases
    close browser


*** Keywords ***
logintoapplication   #this is a user defined keyword
    click link  xpath://a[contains(text(),'Login')]
    input text  class:class="_2IX_2- VJZDxU"        kumar.kiran744@gmail.com
    input text  class="_2IX_2- _3mctLh VJZDxU"      kiran@391
    click element      xpath://body/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]


    # inorder to run the robotic testcase file we need to run it in terminal
    # by giving robot directoryname\filename.robot
    # cls to clear the console
    # uparrow to repeat the command





