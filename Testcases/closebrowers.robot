*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
multiplebrowserstest
    open browser    http://demowebshop.tricentis.com/register   chrome
    maximize browser window

    open browser    https://google.com      chrome
    maximize browser window

    #close browser   #this closes only the recent browser
    close all browsers  #this closes all the browsers
