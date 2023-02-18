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
cell_letter = ''
cell_number = 0
x = 0
y = 0
ch = '00'
for cell_letter in alphabet:
    for cell_number in range(1, 21):
        cell_fill = ''
        cell_fill = sheet_active[f'{cell_letter}{cell_number}'].fill.start_color.index #Получаем цвет ячейки
        
        cell_ch = cell_fill.lstrip(ch)
        #cell_fill = '#' + cell_fill
        
        #cell_ch = '#' + cell_ch
        for x in range(21):
            for y in range(21):
                print(f'#',f'{cell_fill}')
                draw.rectangle((x, y, x, y), fill=f'{cell_ch}')
                print(x,y)
im.show()