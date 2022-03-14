*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
MultipleBrowserTest
    open browser    https://google.com  chrome
    maximize browser window
    sleep   3
    open browser     https://bing.com    chrome
    maximize browser window
    sleep   3
    switch browser  1       #switching to browser 1
    ${title1}=  get title   #getting the title
    log to console  ${title1}
    switch browser  2   #switching to browser 2
    ${title2}=  get title   #getting the title
    log to console  ${title2}

    sleep  3
    close all browsers

