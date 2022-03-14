*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://testautomationpractice.blogspot.com/
${browser}      chrome

*** Test Cases ***
Alerttestcase
    open browser    ${url}      ${browser}
    maximize browser window
    click element   xpath://*[@id="HTML9"]/div[1]/button
    #handle alert    accept      #clicks ok on the alert ribbon
    #handle alert    dismiss    #clicks on cancel button on the alert ribbon
    #handle alert    leave       #it just leaves the alert without doing anything
    alert should be present     Press a button!  #checks whether the above text is present in the alert or not




