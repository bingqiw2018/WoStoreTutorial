#coding=utf-8 
'''
Created on 2018年4月24日

@author: bingqiw
'''
import src.datasource.DBManager as db
import pandas as pd
import datetime

import chardet

from _mysql import NULL
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

def getSaleInfoForAllProvice(year, month, date_num):
    
    if year == NULL or month == NULL:
        print "参数不能为空"
    else:
        try:
            qry_date_str = year+month+"%"
            sql = "SELECT  SUBSTR(UPDATE_TIME,0,6) AS NEW_DATE, PROV_ID, PROV_NAME,COUNT(*) AS TOTAL FROM SYNC_SALE_ORDER_INFO WHERE UPDATE_TIME LIKE '"+qry_date_str+"' AND PROV_ID IS NOT NULL GROUP BY SUBSTR(UPDATE_TIME,0,6), PROV_ID, PROV_NAME ORDER BY PROV_ID;"
            df01 = db.qry_sql(db.hbase_con,sql)
            pro_num_01 = df01.shape[0]
            print ("共获得查询省数量：{}".format(pro_num_01))
            
            sql = "SELECT PROV_ID, PROV_NAME, COUNT(*) AS DATE_SUM FROM ( SELECT  SUBSTR(UPDATE_TIME,0,8) AS NEW_DATE, PROV_ID, PROV_NAME, DATA_SOURCE, COUNT(*) AS TOTAL FROM SYNC_SALE_ORDER_INFO WHERE UPDATE_TIME LIKE '"+qry_date_str+"' AND PROV_ID IS NOT NULL AND DATA_SOURCE = '1' GROUP BY SUBSTR(UPDATE_TIME,0,8), PROV_ID, PROV_NAME, DATA_SOURCE) GROUP BY PROV_ID, PROV_NAME ORDER BY PROV_ID;"
            df02 = db.qry_sql(db.hbase_con,sql)
            df = pd.concat([df01,df02],axis=1,ignore_index=False)
            pro_num_02 = df.shape[0]
            df['DATE_SUM'] = df['DATE_SUM'].apply(pd.to_numeric)
            data01 = df.loc[df['DATE_SUM'] == date_num]
            data02 = df.loc[df['DATE_SUM'] != date_num]
            
            num01 = data01.shape[0]
            num02 = data02.shape[0]
            
            if pro_num_02 !=  pro_num_01:
                print ("{}年{}月，数据有丢失:{}".format(year,month,(pro_num_01 - pro_num_02)))
            else:
                print ("{}年{}月，数据完整:{}".format(year,month,pro_num_02))
            
            print "完整数据省份:{};不完整数据省份:{}".format(data01.shape[0],data02.shape[0])
            
            name = 'd:/tmp/wo_store_'+datetime.datetime.now().strftime('%Y-%m-%d')+'.xlsx'
            
            print df.head()
            
            df.to_excel(name,index=False,header=None)

        finally:
            db.hbase_con.close()  
        
        
        
        