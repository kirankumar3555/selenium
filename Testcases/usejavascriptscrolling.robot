*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Scrollingdownapage
    open browser    https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/      chrome
    maximize browser window
    #execute javascript  window.scrollTo(0,1500)     #this will scroll the bar down to 1500 pixels vertically.(horizontal scroll,vertical scroll)
    #now if we want to scroll our page only till a specific element
    #scroll element into view    xpath://*[@id="example2"]/tbody/tr[82]/td[2]/a     #this scrolls till cub in the webpage
    #now if we want to scroll till the end of the page then
    execute javascript  window.scrollTo(0,document.body.scrollHeight)   #this will scroll the page till the end
    #now if we want to reverse and get back to top of the page then
    sleep   5
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)
