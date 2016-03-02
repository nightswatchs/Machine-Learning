#---coding: utf-8---
import xlrd
def recom():
    workbook = xlrd.open_workbook('A0101a.xls')
    work = workbook.sheets()[0]
    dicts = {}

    for row in range(7,work.nrows):
        region = work.cell(row,0).value.encode('utf-8')
        dicts[region] = []
        for col in range(1, work.ncols):
            dicts[region].append(work.cell(row, col).value)
    return dicts

