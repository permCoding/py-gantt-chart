import os


# pip install xlwt xlrd xlutils
import xlrd

rb = xlrd.open_workbook('grafik.xlsx')
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)[0]

lines = [sheet.row_values(row) for row in range(sheet.nrows)]
for line in lines[7:]:
	print(*line)


os.system('pause')