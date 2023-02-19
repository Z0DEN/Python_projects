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
sheet_active = workbook[sheets_list[0]]
x = 0
y = 0
for cell_letter in alphabet:
    y += 1
    x = 0
    for cell_number in range(1, 21):
        cell_fill = sheet_active[f'{cell_letter}{cell_number}'].fill.start_color.index #Получаем цвет ячейки
        cell_hex ='#' + cell_fill[2:8]
        draw.rectangle((x, y-1, x, y-1), fill=f'{cell_hex}')
        x += 1
im.show()