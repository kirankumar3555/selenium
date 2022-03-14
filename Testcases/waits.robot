*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${browser}              chrome
${url}          http://demowebshop.tricentis.com/register

*** Test Cases ***
Waittesting
    #${speed}=   get selenium speed
    #log to console   ${speed}
    open browser    ${url}      ${browser}
    # set selenium timeout    10 seconds      # now the wait until statement waits for 10 seconds irrespective of it's repspective time given
    wait until page contains    Register    #it waits for 5 seconds in checking if it exists then process continues else testcase fails
    set selenium speed  1 second
    select radio button         Gender         M
    set selenium implicit wait  10 seconds
    input text  name:FirstName      kiran
    input text  name:LastName       rayabharapu
    input text  name:Email          kumar.kiran744@gmail.com
    input text  name:Password       kiran#121
    input text  name:ConfirmPassword    kiran#121





