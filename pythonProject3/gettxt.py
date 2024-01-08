import xlwings as xw
import openpyxl as op
import  pandas as pd
import xlwt
def open_data(num:str):
    file='C:/Users/24333/Desktop/python/pythonProject3/Solomon_VRPTW-master/solomon_100/'
    filename=file+num+'.txt'
    with open(filename,'r') as f:
        content=f.readlines()
    data=content[10:]
    global x_loc
    x_loc=[]
    global y_loc
    y_loc=[]
    for i in range(len(data)):
        a=data[i]
        num=a.split('      ')
        x_loc.append(num[1])
        y_loc.append(num[2])
def write_excel(a:int):
    # 创建一个新的Excel文件
    workbook = xlwt.Workbook()
    # 创建一个工作表
    sheet1 = workbook.add_sheet('Sheet1')
    # 将列表1的数据写入Excel文件
    for i in range(len(x_loc)):
        sheet1.write(i, 0,x_loc[i])
    # 将列表2的数据写入Excel文件
    for i in range(len(y_loc)):
        sheet1.write(i, 1, y_loc[i])
    file='C:/Users/24333/Desktop/python/pythonProject3/Solomon_VRPTW-master/excel/'
    filename=file+'r'+str(a)+'.xls'
    print(filename)
    workbook.save(filename)
def create_excel():
    import xlwings as xw
    app = xw.App(visible=True, add_book=False)
    file_path = r"C:\Users\24333\Desktop\python\pythonProject3\Solomon_VRPTW-master\excel"
    for i in range(56):
        workbook = app.books.add()
        # 生成文件名字
        fileName = r"\r" + str(i) + ".xls"
        workbook.save(file_path + fileName)
        workbook.close()
    app.quit()
def open_write():
    for i in range(9):
        a='C'+str(101+i)
        print(a)
        open_data(a)
        write_excel(i)
create_excel()
open_write()