#---coding: utf-8---
import xlrd
work = xlrd.open_workbook('A0101a.xls',formatting_info = True).sheets()[0]

data = []
#for i in range(1, work.ncols):
#    data.append(work.cell(6, i).value.encode('utf-8'))

#for content in data:
#    print content,
merges = work.merged_cells
sorts = sorted(merges, key=lambda m:m[0])
print merges
print sorts
for i in sorts:
    if i[1] == 7:
        print i
        data.append(work.cell(i[0],i[2]).value.encode('utf-8'))
    else:
        pass
for j in data:
    print j
