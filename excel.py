import xlwt
import xlrd

# wb = xlwt.Workbook(encoding='ascii')
# ws = wb.add_sheet('wg')
# ws.write(0, 0, label='hs')
# ws.write(0, 1, label='wd')
# ws.write(1, 0, label='你好啊')
# wb.save('E://xt.xls')



datas = xlrd.open_workbook('E://xt.xls')
table = datas[0]
r=datas[2]
print(table.nrows)
print(table.ncols)
print(table.row_values(0))
print(table.col_values(0))
print(r.cell(1,1).value)
print(r.cell(0,0).value)