#---coding: utf-8---
import xlrd
work = xlrd.open_workbook('A0101a.xls').sheets()[0]

data = []

for i in range(1, work.ncols):
    data.append(work.cell(6, i).value.encode('utf-8'))

for content in data:
    print content,
