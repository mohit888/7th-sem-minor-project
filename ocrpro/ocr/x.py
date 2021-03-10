from pandas import *
xls = ExcelFile('OCR.xlsx')
data = xls.parse(xls.sheet_names[0])
#print(data.to_dict())
data = data.to_dict()
print(data.data())