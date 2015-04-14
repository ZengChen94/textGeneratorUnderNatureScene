#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        导出数据库数据.py
# Purpose:
#
# Author:      SQ1000
#
# Created:     08-02-2012
#-------------------------------------------------------------------------------

import os
import pymssql
import sys

class MSSQLHelper:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQLHelper(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"))
        resList =  cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql.encode("utf8"))
        self.conn.commit()
        self.conn.close()


def RemoveDirectory (top):
    while 1:
        if os.path.exists(top):
            if len(os.listdir(top)) == 0:
                os.rmdir (top)
                break
            else:
                for root, dirs, files in os.walk(top, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
        else:
            break

def export(db,user,password):
    """导出数据库"""
    #得到当前脚本的执行目录
    currentDirectory = os.getcwd()

    #查看是否已经存在备份目录，如果有则删除，没有则新建目录
    backUpDirectory = "%s\\%s" %( currentDirectory,db+"Backup")
    if os.path.exists(backUpDirectory):
        RemoveDirectory(backUpDirectory)
        os.mkdir(backUpDirectory)
    else:
        os.mkdir(backUpDirectory)

    #得到要到处的数据库的所有表
    ms = MSSQLHelper(host="localhost",user=user,pwd=password,db=db)
    for (name,) in ms.ExecQuery("select name from sysobjects where xtype='U'"):
        currentTablePath = "%s\\%s.txt"%(backUpDirectory,name)
        r = os.popen('BCP %s..%s out %s -c -U"%s" -P"%s"' % (db,name,currentTablePath,user,password))
        print r.read()
        r.close()

def inport(db,user,password):
    """导入数据库"""
    #得到当前脚本的执行目录
    currentDirectory = os.getcwd()

    #查看是否已经存在备份目录，如果有则删除，没有则新建目录
    backUpDirectory = "%s\\%s" %( currentDirectory,db+"Backup")
    if os.path.exists(backUpDirectory):
        #得到要到处的数据库的所有表
        ms = MSSQLHelper(host="localhost",user=user,pwd=password,db=db)
        for (name,) in ms.ExecQuery("select name from sysobjects where xtype='U'"):
            currentTablePath = "%s\\%s.txt"%(backUpDirectory,name)
            r = os.popen('BCP %s..%s in %s -c -U"%s" -P"%s"' % (db,name,currentTablePath,user,password))
            print r.read()
            r.close()


def main():

    db = "textgenerator"
    user = "root"
    password = "zc1210wh1019"

    #这边可以根据不同的参数选择不同的操作
    #我是使用了两个文件，一个是导入一个导出
    inport(db,user,password)

if __name__ == '__main__':
    main()

    print u"\n导出完成...\n回车键退出"
    raw_input()
