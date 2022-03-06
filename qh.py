# handling alerts
# alerts are blocking in nature until we handle them we can't perform any operation on the browser
import pandas as pd
import xlrd
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

loc=("C:/Users/kumar/OneDrive/Desktop/selenium/Book_1.xlsx")
wb=xlrd.open_workbook(loc) # opening the workbook(contains all the sheets of excel)
sheet=wb.sheet_by_index(0) # taking a specific sheet using index
p1=sheet.cell(1,0).value # taking a specific value of a cell inside an excel sheet
print(p1)
print(sheet.nrows) # printing the no of rows in that sheet
print(sheet.ncols) # printing the no of columns in that sheet
for i in range(sheet.nrows): # printing all the row values inside the excel sheet
    p2=sheet.cell(i,0).value
    print(p2)









