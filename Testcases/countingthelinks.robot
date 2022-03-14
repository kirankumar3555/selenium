*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
countinglinkstestcases
    open browser    https://www.selenium.dev/   chrome
    maximize browser window
    ${alllinkscount}=    get element count      xpath://a
    log to console  ${alllinkscount}

    @{linkitems}=    create list

    FOR     ${i}    IN  RANGE   1   ${alllinkscount}+1
    ${linktext}=        get text    xpath:(//a)[${i}]
    log to console  ${linktext}
    END


    FOR     ${item}     IN    RANGE  1  ${}