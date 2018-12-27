#coding=utf-8 
'''
Created on 2018年4月20日

@author: bingqiw
'''
import pandas as pd
import MySQLdb as md
import datetime

prod_con  = md.connect(host='10.191.33.31', port=3306,user='prodqry', passwd='123456', db='prod')
sysman_con = md.connect(host='10.191.33.31', port=3306,user='sysmanqry', passwd='123456', db='sysman')
report_con = md.connect(host='10.191.33.31', port=3306,user='reportqry', passwd='123456', db='report')
param_con = md.connect(host='10.191.33.30', port=3306,user='paramqry', passwd='123456', db='param')
hbase_con =  md.connect(host='10.191.5.227', port=3307,user='root', passwd='Bata@Sale!', db='phoenix')

def test_sql(svc_con,sql):
    try:
        start = datetime.datetime.now()
        df = pd.read_sql(sql, con=svc_con) 
        print df.shape
        svc_con.close()
    finally:
        svc_con.close()  
        end = datetime.datetime.now()
        total = end - start
        print (" cost time = start:{}".format(start))
        print (" cost time =   end:{}".format(end))
        print (" cost time = total:{}".format(total))
        print "end"
def load_customer(svc_con,sql):
    try:
        start = datetime.datetime.now()
        df = pd.read_sql(sql, con=svc_con) 
        end = datetime.datetime.now()
        print ("get data size {} ; cost time {}".format(df.shape[0], (end - start)))
        
        start = datetime.datetime.now()
        name = 'd:/tmp/customer'+datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')+'.xlsx'
        df.to_excel(name,index=False)
        print ("export data size {} ; cost time {}".format(df.shape[0], (end - start)))
        end = datetime.datetime.now()
    finally:
        svc_con.close()    

qry_date_str = "201804"
sql = "SELECT SUBSTR(UPDATE_TIME,0,6) AS NEW_DATE, PROV_ID, PROV_NAME,COUNT(*) AS TOTAL FROM SYNC_SALE_ORDER_INFO WHERE UPDATE_TIME LIKE '"+qry_date_str+"%' AND PROV_ID IS NOT NULL GROUP BY SUBSTR(UPDATE_TIME,0,6), PROV_ID, PROV_NAME;"
test_sql(hbase_con,sql)


