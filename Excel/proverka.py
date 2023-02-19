import openpyxl
from PIL import Image, ImageDraw
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import numpy as np

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

im = Image.new('RGB', (20, 20), (255, 255, 255))
draw = ImageDraw.Draw(im)

workbook = openpyxl.load_workbook('/home/blesk/GitHub/Python_projects/img-to-xlsx.xlsx')
sheets_list = workbook.sheetnames
x = 0
y = 0
for cell_letter in alphabet:
    for cell_number in range(1, 21):
            cell_fill = sheet_active[f'{cell_letter}{cell_number}'].fill.start_color.index #Получаем цвет ячейки
            cell_ch ='#' + cell_fill[2:8]
            draw.rectangle((x, y, x, y), fill=f'{cell_ch}')
            x += 1
            y += 1
im.show()