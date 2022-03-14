*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      http://demowebshop.tricentis.com/register
${browser}      chrome

*** Test Cases ***
Radiobuttontestcase
    open browser    ${url}      ${browser}
    maximize browser window
    set selenium speed     2
    select radio button     Gender        M         #name    value
    select radio button     Gender        F         #name     value
    unselect radio button   Gender        F
    close browser
