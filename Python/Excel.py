#-*- coding: utf-8 -*-
#coding:utf-8
import sys,os,time
import xlwt,xlrd,xlutils
from xlutils.copy import copy

def init():
    if not os.path.exists(u'版本发布说明书.xls'):
        create_f = xlwt.Workbook(encoding = 'utf-8')
        table = create_f.add_sheet('info',cell_overwrite_ok=True)
        table.write(0,0,'项目名称')
        table.write(0,1,'系统版本号')
        table.write(0,2,'代码路径')
        table.write(0,3,'SVN版本号')
        table.write(0,4,'变更内容')
        table.write(0,5,'发布日期')
        table.write(0,6,'变更申请人')
        table.write(0,7,'变更实施人')
        table.write(0,8,'变更是否成功')
        table.write(0,9,'备注')
        create_f.save(u'版本发布说明书.xls')


def add_data(PejectName,Version_Name,SvnCode,Svn_VERSION,Change_INFO,RequestAuth,Release_Auth,ChangeYesNo):
    init()
    date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print (date)
    data = xlrd.open_workbook(u"版本发布说明书.xls")
    nrows = data.sheet_by_index(0).nrows
    new_excel = xlutils.copy.copy(data)
    AddNew = new_excel.get_sheet(0)
    AddNew.write(nrows,0,PejectName.decode('utf-8'))
    AddNew.write(nrows,1,Version_Name.decode('utf-8'))
    AddNew.write(nrows,2,SvnCode.decode('utf-8'))
    AddNew.write(nrows,3,Svn_VERSION.decode('utf-8'))
    AddNew.write(nrows,4,Change_INFO.decode('utf-8'))
    AddNew.write(nrows,5,date)
    AddNew.write(nrows,6,RequestAuth.decode('utf-8'))
    AddNew.write(nrows,7,Release_Auth.decode('utf-8'))
    AddNew.write(nrows,8,ChangeYesNo.decode('utf-8'))
    # AddNew.write(nrows,9,bak.decode('gbk'))

    new_excel.save(u'版本发布说明书.xls')
    print ('Successful')

def read_f():
    #获取一个工作表
    data = xlrd.open_workbook("版本发布说明书.xls")

    #table = data.sheets()[0]  #通过索引获取
    #table = data.sheet_by_index(1) #通过索引获取
    table = data.sheet_by_name(u'info') #通过表名获取
    #print table

    # table.row_values(i) 获取整行数值
    # table.col_values(i) 获取整列数值

    nrows = table.nrows #获取整行数
    print (nrows)
    # ncols = table.nclos 获取整列值

    #循环行、列 表数据
    for i in range(nrows):
        print (table.row_values(i))

    #单元格
    cell_A1 = table.cell(0,0).value
    #call_B1 = table.cell(2.3).value
    print (cell_A1)

    #使用行列索引
    cell_A2 = table.row(0)[1].value
    # cell_A3 = table.col(1)[0].value
    print (cell_A2)

    #简单的写入
    # row = 0
    # col = 0
    # #类型 0 empty.1 string .2 number.3 date.4 boolean.5 error
    # ctype =1
    # value = 'PROJECTNAME'
    # xf = 'VERSION'
    # table.put_cell(row,col,ctype,value,xf) #不行啊


if __name__ == "__main__":
    # try:
        PejectName,Version_Name,SvnCode,Svn_VERSION,Change_INFO,RequestAuth,Release_Auth,ChangeYesNo = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8]
        add_data(PejectName,Version_Name,SvnCode,Svn_VERSION,Change_INFO,RequestAuth,Release_Auth,ChangeYesNo)
        print ('Done')

    # except:
    #     print """\
    #     Usage: python {0} argv1 argv2 argv3 argv4 argv5\
    #     """.format(sys.argv[0])
