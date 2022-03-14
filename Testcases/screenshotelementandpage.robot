*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
screenshotelementandpage
    open browser    https://opensource-demo.orangehrmlive.com/  chrome
    input text  id:txtUsername  Admin
    input text  id:txtPassword  Admin
    #capture element screenshot  xpath://*[@id="divLogo"]/img    C:/Users/kumar/PycharmProjects/jj/log.png
    #capturing screenshots of element and storing in the directory
    #capture page screenshot    Loginscreenshot.png
    #capturing page screenshots and storing in the directory
    capture element screenshot  xpath://*[@id="divLogo"]/img    logel.png
    #if we did not give directory it just stores in the projectfile itself
    capture page screenshot    Logpagescreenshot.png


