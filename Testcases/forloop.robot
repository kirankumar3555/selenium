*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
#for1
    #FOR     ${i}    IN       1  2   3   4
        #log to console      ${i}
    #END


#for2
#@{list}=   create list   1  2   3   4   4
    #FOR     ${i}    IN  RANGE   @{list}
        #log to console      ${i}
    #END

#for3
    #FOR     ${item}    IN       kiran  vijay   rahul   varma
        #log to console      ${item}
    #END

#for4
    #@{list}=     create list     kiran   ramesh  vijay   poorna
    #FOR     ${i}      IN        @{list}
        #log to console  ${i}
    #END

#for5
    #@{list}=    create list     1   2   3   4
    #FOR     ${i}    IN  @{list}
    #log to console  ${i}
    #exit for loop if    ${i}==2
    #END

