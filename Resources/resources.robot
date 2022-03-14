*** Settings ***
Library     SeleniumLibrary



*** Keywords ***
#launchBrowser                   #this is a userdefined keyword with no arguments
    #open browser    ${url}  ${browser}
    #maximize browser window

launchBrowser           #userdefined keyword with arguments and return values
    [Arguments]    ${appurl}       ${appbrowser}
    open browser    ${appurl}       ${appbrowser}
    maximize browser window
    ${title}=       get title
    [return]    ${title}