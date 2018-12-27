#coding=utf-8 
'''
Created on 2018年4月24日

@author: bingqiw
'''
import src.datasource.DBManager as db
import pandas as pd
from _sqlite3 import Row

def getImportStoreAddress(filename):
    
    data_src = pd.read_excel(filename,header=None,encoding='utf-8')
    df = pd.DataFrame(data_src)
    try:
        print ("开始导入数据：{}".format(df.shape))
        
#         sql = "insert pm_store_import_err(CHNL_ID,TABLE_NAME) VALUES (%s,%s)"
#         param = df.iloc[2:,[5,7]]
#         df = pd.DataFrame(param)
#         arr = []
#         
#         for index, row in df.iterrows():
#             arr.append([row[5],row[7][0:20]])
#         print "数据汇总完毕"
#         print arr
#         db.batch_sql(db.prod_con_test,sql,arr)
#         print "入库完毕"
        
        sql = "select * from pm_store_import_err   ORDER BY CREATE_TIME DESC;"
        df = db.qry_sql(db.prod_con_test, sql)
        print df.head()
    finally:
        db.prod_con_test.close()    
        print "关闭链接"    
            
              