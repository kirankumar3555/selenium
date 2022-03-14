*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      http://demo.automationtesting.in/Windows.html
${browser}      chrome

*** Test Cases ***
Tabbedwindowtestcase
    open browser     ${url}      ${browser}
    maximize browser window
    click element   xpath://*[@id="Tabbed"]/a/button
    sleep   2
    switch window   title=Selenium   # switch to other windows
    click element   xpath://*[@id="main_navbar"]/ul/li[6]/a/span
    close all browsers



