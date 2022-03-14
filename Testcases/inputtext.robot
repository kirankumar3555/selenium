*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Inputtexttestcase
    open browser    http://demowebshop.tricentis.com/register   chrome
    title should be     Demo Web Shop. Register
    ${email}       set variable    id:FirstName
    element should be visible   ${email}
    input text      ${email}        kiran
    sleep  5
    clear element text  ${email}
    close browser

