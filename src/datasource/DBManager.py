#coding=utf-8 
'''
Created on 2018年4月24日

@author: bingqiw
'''
import MySQLdb as md
import datetime
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

# 生产
prod_con  = md.connect(host='10.191.33.31', port=3306,user='prodqry', passwd='123456', db='prod')
sysman_con = md.connect(host='10.191.33.31', port=3306,user='sysmanqry', passwd='123456', db='sysman')
report_con = md.connect(host='10.191.33.31', port=3306,user='reportqry', passwd='123456', db='report')
param_con = md.connect(host='10.191.33.30', port=3306,user='paramqry', passwd='123456', db='param')
hbase_con =  md.connect(host='10.191.5.227', port=3307,user='root', passwd='Bata@Sale!', db='phoenix')

# 测试
prod_con_test  = md.connect(host='10.124.163.136', port=3306,user='root', passwd='root', db='prod', charset="utf8")

def qry_sql(con,sql):
    df = pd.read_sql(sql, con=con) 
    print "Execute:"+sql
    print df.shape
    return df

def do_sql(con, sql, param):
    cur = con.cursor()
    reCout = cur.execute(sql, param)
    print reCout
    con.commit()
    cur.close()

def batch_sql(con, sql, list):    
    cur = con.cursor()
    reCout = cur.executemany(sql, list)
    print reCout
    con.commit()
    cur.close()
    
    
    