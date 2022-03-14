*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Browserkeywordstestcase
    open browser    https://google.com  chrome
    maximize browser window
    ${browser}=  get location   #gives the address of the website
    log to console  ${browser}
    sleep   3

    go to       https://bing.com           # now from google.com we go to bing.com
    ${browser}=  get location
    log to console  ${browser}
    sleep      3

    go back         #now we go back to google.com
    ${browser}=  get location
    log to console  ${browser}
    sleep   3

