# -*- coding:utf-8 -*-
import xlrd
import pymysql

def readExcel(sheet,row,col):
    a=xlrd.open_workbook(".\http.xlsx")#open_workbook方法访问D盘的EXCLE文件
    b=a.sheet_by_name(sheet)#sheet_by_name读叫什么名字的sheet
    c=b.cell_value(row,col) #cell_value取第几行第几列的单元格数据，计数从0序列开始
    return c   #return是一个返回函数，指谁调用readExcel这个方法，就返回C


def mySql(SQL):
    b=pymysql.connect(host="192.168.1.200",port=3306,user="root",passwd="123456",db="db_public")
    sqlResult=b.cursor()#创建一个SQL游标
    c=sqlResult.execute(SQL)
    return c




