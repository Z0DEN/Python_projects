import openpyxl #Подключаем библиотеку <a href="https://openpyxl.readthedocs.io" rel="noopener noreferrer" target="_blank">Openpyxl</a>
path = '/home/blesk/GitHub/Python_projects/img-to-xlsx.xlsx'
workbook = openpyxl.load_workbook(path) #Собственно - читаем сам файл
sheets_list = workbook.sheetnames #Получаем список всех листов в книге
sheet_active = workbook[sheets_list[0]] #Делаем активным самый первый лист в книге
 
cell_fill = sheet_active['A1'].fill.start_color.index #Получаем цвет ячейки
cell_fill = '#' + cell_fill
print(cell_fill) #Выводим на экран :)


        cell_fill = sheet_active[f'{cell_letter}{cell_number}'].fill.start_color.index #Получаем цвет ячейки
