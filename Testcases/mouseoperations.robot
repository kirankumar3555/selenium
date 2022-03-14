*** Settings ***
Library     SeleniumLibrary
*** Test Cases ***
Mouseoperations
    open browser    http://swisnl.github.io/jQuery-contextMenu/demo.html    chrome
    maximize browser window
    open context menu   xpath:/html/body/div[1]/section/div/div/div/p/span  #right click operation which displays context menu
    sleep   3

    go to   https://testautomationpractice.blogspot.com/
    double click element    //*[@id="HTML10"]/div[1]/button  #double click on the element
    sleep   3

    go to   http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    drag and drop       id:box1         id:box101   #dragging and dropping id:box1 is source object id and box101 is destination object id
    sleep  3
    close browser
