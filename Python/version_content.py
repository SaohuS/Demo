# -*- coding:utf-8 -*-
#coding=utf-8
import pymysql
import os
import sys
# reload(sys)
# defaultencoding = 'utf-8'
# # 解决编码问题ASCII
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)
# print sys.getdefaultencoding()
# #连接数据库
conn = pymysql.connect(host="172.16.26.40",port=3306,user="root",passwd="",db="version_content",charset='utf8')
cur = conn.cursor()

def getonedata(DataID):
    #获取一个数据
    cur.execute("SELECT * FROM file_info WHERE fileName='%s';"%DataID)
    onedata = cur.fetchone()
    print 'ID'.decode('utf8'),onedata[0],'USER-ID',onedata[1],'FILE-SIZE',onedata[2],'FILE-NUM',onedata[3]
    conn.close()

def GetAllData():
    #获取所有记录列表
    cur.execute("SELECT * FROM version_tb")
    onedata = cur.fetchall()
    for row in onedata:
        print row[0],row[1],row[2],row[3],row[4],row[5]
    conn.close()

def CreateTable():
    # cur.execute('create database ;')
    sqltable = '''create table if not exists `version_tb`(
                `version_id` int unsigned auto_increment,
                `project_name` char(100) not null,
                `project_no` varchar(50) not null,
                `change_info` varchar(100) not null,
                `subversion_no` int not null,
                `release_time` datetime,
                `remarks` varchar(50) not null,
                primary key (`version_id`)
                )engine=InnoDB default charset=utf8;'''
    # print sqltable
    cur.execute(sqltable)
    conn.close()

#检查数据库是否存在
def Inspect():
    try:
        cur.execute("select * from version_tb")
        return True
    except Exception:
        print 'no search mysql database version_tb'
        return False

if __name__ == "__main__":
    # 检查表是否存在
    if not Inspect():
        # 创建表
        CreateTable()
    else:
        project_name,project_no,change_info,subversion_no,release_time,remarks = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]
        print '---- version_content already ----'
        print '---- Start insert data ----'
        # 插入数据 解码unicode
        info = '''insert into version_tb (project_name,project_no,change_info,subversion_no,release_time,remarks)
                values ('%s','%s','%s','%s','%s','%s');'''%(unicode(project_name,'utf-8'),project_no,unicode(change_info,'utf-8'),subversion_no,release_time,unicode(remarks,'utf-8'))
        cur.execute(info)
        conn.commit()
        conn.close()
        print '---- End insert data  ----'
