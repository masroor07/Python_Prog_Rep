#xlrd is a library for reading data and formatting information from Excel files
import xlrd
#path of the excel file that you wanna read
loc= ("C:\\Users\\HP\\Desktop\\Python\\Class.xls")

#opening workbook
workbook= xlrd.open_workbook(loc)
#opening a particular sheet from the excel file
s = workbook.sheet_by_index(0)
#printing the value of index 0
print(s.cell_value(0,0))
