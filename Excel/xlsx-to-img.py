import openpyxl
from PIL import Image
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import numpy as np

square = np.zeros((255, 255))

for i in range (0, 255, 1):
    print(i)
    x = 0
    for j in range (0, 255, 1):
        square[i:i+1, j:j+1] = x
        x += 1
        


square_img = Image.fromarray(square)
square_img.show()