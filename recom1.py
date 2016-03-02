#---coding: utf-8---
import xlrd

#打开文件
workbook = xlrd.open_workbook('A0101a.xls')

work = workbook.sheets()[0]

dicts = {}
data = []
#i = 0
# 个数确定
for row in range(7,work.nrows):
    region = work.cell(row,0).value
    dicts[region] = []
#    i += 1
    for col in range(1, work.ncols):
        dicts[region].append(work.cell(row, col).value)

#for region, number in dicts.items():
#    print region,number
print dicts
