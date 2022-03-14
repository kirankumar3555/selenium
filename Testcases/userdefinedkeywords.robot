*** Settings ***
Library     SeleniumLibrary
Resource       ../Resources/resources.robot

*** Variables ***
${url}          https://testautomationpractice.blogspot.com/
${browser}      chrome

*** Test Cases ***
keywordtestcase
    #launchBrowser       ${url}      ${browser}    #userdefined keyword with arguments passed
    ${result}=   launchBrowser       ${url}      ${browser}
    log to console  ${result}
    log     ${result}
    select frame    frame-one1434677811
    input text  name:RESULT_TextField-1     kiran
    input text  name:RESULT_TextField-2     rayabharapu






