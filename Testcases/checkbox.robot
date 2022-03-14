*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://www.w3.org/TR/wai-aria-practices-1.1/examples/checkbox/checkbox-2/checkbox-2.html

*** Test Cases ***
CheckBoxTestcase
    open browser    ${url}      ${browser}
    maximize browser window
    set selenium speed  1           #each statement gets executed after 3 seconds
    unselect checkbox   cond1       #unselect checbox
    select checkbox     cond1       #select checkbox
    select checkbox     cond2
    unselect checkbox   cond1
    unselect checkbox   cond2
    close browser
