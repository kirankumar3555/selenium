*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${browser}      chrome
${url}      http://demowebshop.tricentis.com/books

*** Test Cases ***
dropdowntestcase
    open browser    ${url}      ${browser}
    maximize browser window
    set selenium speed      3
    click element   id:products-orderby
    select from list by label       products-orderby        Name: A to Z
    sleep   5
    select from list by index       products-pagesize       2
    close browser
