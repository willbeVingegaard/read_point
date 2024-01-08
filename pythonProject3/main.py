# coding=utf-8
import xlrd
import random
import turtle
import xlwings as xw
import openpyxl as op
import  pandas as pd
import xlwt
n=20
r_num=4
def read(num:int):
    file='C:/Users/24333/Desktop/python/pythonProject3/Solomon_VRPTW-master/excel/'
    filename=file+'c'+str(num)+'.xls'
    wb = xlrd.open_workbook(filename)
    ws=wb.sheet_by_index(0)
    global data
    data=[]
    rows=ws.nrows
    for i in range(rows):
        row=ws.row_values(i)
        data.append(row)
    print(data)
def true_charge():#按照权值分配充电桩
    result=sq_4(data)
    a=0
    for i in range(r_num):
        a+=result[i]
    for j in range(r_num):
        result[j]=round((result[j]/a)*20)
    print(result)
    return result
def true_charge_c():
    result=sq_16(data)
    max_n=[]
    for i in range(4):
        num_max=result.index(max(result))
        max_n.append(num_max)
        del result[num_max]
    return result
def sq_4(data):
    a=0
    b=0
    c=0
    d=0
    for i in range(len(data)):
        if data[i][0]<50 and data[i][1]<50:
            a+=1
        elif data[i][0]>50 and data[i][1]<50:
            b+=1
        elif data[i][0]<50 and data[i][1]>50:
            c+=1
        elif data[i][0]>50 and data[i][1]>50:
            d+=1
    result=[]
    result.append(a)
    result.append(b)
    result.append(c)
    result.append(d)
    return result
def sq_16(data):
    a,b,c,d,e,f,g,h,z,j,k,l,m,n,o,p=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    for i in range(len(data)):
        if data[i][0]<25 and data[i][1]<25:
            a+=1
        elif data[i][0]<25 and data[i][1]<50:
            b+=1
        elif data[i][0]<25 and data[i][1]<75:
            c+=1
        elif data[i][0]<25 and data[i][1]<100:
            d+=1
        elif 25 < data[i][0] < 50 and data[i][1] < 25:
            e+= 1
        elif 25 < data[i][0] < 50 and data[i][1] < 50:
            f += 1
        elif 25 < data[i][0] < 50 and data[i][1] < 75:
            g+= 1
        elif 25 < data[i][0] < 50 and data[i][1] < 100 :
            h += 1
        elif 50 < data[i][0] < 75 and data[i][1] < 25:
            z+= 1
        elif 50 < data[i][0] < 75 and data[i][1] < 50:
            j+=1
        elif 50 < data[i][0] < 75 and data[i][1] < 75:
            k+=1
        elif 50 < data[i][0] < 75 and data[i][1] < 100:
            l+=1
        elif 75 < data[i][0] < 100 and data[i][1] < 25:
            m+=1
        elif 75 < data[i][0] < 100 and data[i][1] < 50:
            n+=1
        elif 75 < data[i][0] < 100 and data[i][1] < 75:
            o+=1
        elif 75 < data[i][0] < 100 and data[i][1] < 100:
            p+=1
    result=[]
    result.append(a)
    result.append(b)
    result.append(c)
    result.append(d)
    result.append(e)
    result.append(f)
    result.append(g)
    result.append(h)
    result.append(z)
    result.append(j)
    result.append(k)
    result.append(l)
    result.append(m)
    result.append(n)
    result.append(o)
    result.append(p)
    print(result)
    return result
def random_charge_C(n:int,result):#充电桩
    global rd
    rd = []
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(0,25))
        list_1.append(random.randint(0,25))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(0,25))
        list_1.append(random.randint(25,50))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(0,25))
        list_1.append(random.randint(50,75))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(0,25))
        list_1.append(random.randint(75,100))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(25,50))
        list_1.append(random.randint(0,25))
        rd.append(list_1)
    for i in range(2):
        list_1 = []
        list_1.append(random.randint(25,50))
        list_1.append(random.randint(25,50))
        rd.append(list_1)
    for i in range(2):
        list_1 = []
        list_1.append(random.randint(25,50))
        list_1.append(random.randint(50,75))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(25,50))
        list_1.append(random.randint(75,100))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(50,75))
        list_1.append(random.randint(0,25))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(50,75))
        list_1.append(random.randint(25,50))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(50,75))
        list_1.append(random.randint(50,75))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(50,75))
        list_1.append(random.randint(75,100))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(75,100))
        list_1.append(random.randint(0,25))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(75,100))
        list_1.append(random.randint(25,50))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(75,100))
        list_1.append(random.randint(50,75))
        rd.append(list_1)
    for i in range(1):
        list_1 = []
        list_1.append(random.randint(75,100))
        list_1.append(random.randint(75,100))
        rd.append(list_1)
    num=true_charge_c()
    list_1 = []
    list_1.append(random.randint(0,100))
    list_1.append(random.randint(0,100))
    rd.append(list_1)

def random_charge(n:int,result):
    global rd
    rd = []
    for i in range(result[2]):
        list=[]
        x=random.randint(50,100)
        y=random.randint(50,100)
        list.append(x)
        list.append(y)
        rd.append(list)
    for i in range(result[0]):
        list=[]
        x=random.randint(0,50)
        y=random.randint(50,100)
        list.append(x)
        list.append(y)
        rd.append(list)
    for i in range(result[3]):
        list=[]
        x=random.randint(50,100)
        y=random.randint(0,50)
        list.append(x)
        list.append(y)
        rd.append(list)
    for i in range(result[1]):
        list=[]
        x=random.randint(0,50)
        y=random.randint(0,50)
        list.append(x)
        list.append(y)
        rd.append(list)
def intersection(rd,data):#查找重复的点
    global list_same
    list_same=[]
    for i in range(len(rd)):
        for j in range(len(data)):
            if rd[i][0]==data[j][0] and rd[i][1]==data[j][1]:
                list_same.append(i)


    return list_same
def delsame(list_same):#删除重复的点
    if len(list_same)>0:
        for i in range(len(list_same)):
            print(list_same[i])
            rd[i][0]=random.randint(0, 80)
            rd[i][1]=random.randint(0, 80)
def darwing(rd,data):#画点
    turtle.speed(0)
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.forward(400)
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    turtle.left(90)
    turtle.forward(400)
    for i in range(len(rd)):
        turtle.up()
        x=rd[i][0]*4
        y=rd[i][1]*4
        turtle.goto(x,y)
        turtle.down()
        turtle.dot(5,'red')
    for j in range(len(data)):
        turtle.up()
        turtle.goto(data[j][0]*4,data[j][1]*4)
        turtle.down()
        turtle.dot(5,'blue')
def open_data(num:str):
    file='C:/Users/24333/Desktop/python/pythonProject3/Solomon_VRPTW-master/solomon_100/'
    filename=file+num+'.txt'
    with open(filename,'r') as f:
        content=f.readlines()
    data=content[10:]
    print(data)
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
    filename=file+'c'+str(a)+'.xls'
    print(filename)
    workbook.save(filename)
def create_excel():

    app = xw.App(visible=True, add_book=False)
    file_path = r"C:\Users\24333\Desktop\python\pythonProject3\Solomon_VRPTW-master\excel"
    for i in range(56):
        workbook = app.books.add()
        # 生成文件名字
        fileName = r"\c" + str(i) + ".xls"
        workbook.save(file_path + fileName)
        workbook.close()
    app.quit()
def open_write():
    for i in range(9):
        a='C'+str(201+i)
        print(a)
        open_data(a)
        #write_excel(i)
        read(i)
        sq_4(data)
        random_charge(20, true_charge())
        print(rd)
        intersection(rd, data)
        delsame(intersection(rd, data))
        print(rd)
        darwing(rd, data)
open_write()


