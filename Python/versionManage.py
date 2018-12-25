#!/usr/bin/python
#coding:utf-8
#author:wusi

import xlwt,xlrd,xlutils
from xlutils.copy import copy
import os,sys,time

def init():
	if not os.path.exists(u"版本发布说明.xls"):
		f = xlwt.Workbook(encoding = 'utf-8')
		w = f.add_sheet(u"版本发布说明",cell_overwrite_ok=True)
		w.write(0,0,u"产品项目名")
		w.write(0,1,u"发布产品版本号")
		w.write(0,2,u"变更详细说明")
		w.write(0,3,u"svn版本号")
		w.write(0,4,u"发布日期")
		w.write(0,5,u"备注")
		f.save(u"版本发布说明.xls")	

def add(proName,proVersion,proInfo):
	init()
	date = time.strftime("%Y-%m-%d %H:%M%S",time.localtime())
	f = xlrd.open_workbook(u"版本发布说明.xls",formatting_info=True)
	nrows = f.sheet_by_index(0).nrows
	d = xlutils.copy.copy(f)
	w = d.get_sheet(0)
	w.write(nrows,0,proName0
			)
	w.write(nrows,1,proVersion.decode('utf-8'))
	w.write(nrows,2,proInfo.decode('utf-8'))
	w.write(nrows,3,proSvnVersion.decode('utf-8'))
	w.write(nrows,4,date)
	d.save(u"版本发布说明.xls")

if __name__ == "__main__":
	try:
		proName, proVersion, proInfo, proSvnVersion = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
		add(proName,proVersion,proInfo)
	except:
		print """\
	Usage: python {0} arg1 arg2 arg3 arg4\
			""".format(sys.argv[0])
