*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html
${browser}      chrome

*** Test Cases ***
Frametestcase
    open browser    ${url}  ${browser}
    sleep   3
    select frame    packageListFrame  #selecting frame with packagelistframe name
    click link      org.openqa.selenium     #clicking the link with name
    unselect frame      #unselecting the frame to select another frame

    sleep   3
    select frame    packageFrame
    click link      Capabilities
    unselect frame

    sleep   3
    select frame    classFrame
    click link      Index
    unselect frame



