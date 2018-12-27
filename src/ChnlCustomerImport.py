#coding=utf-8 
'''
Created on 2018年7月18日

@author: bingqiw
'''
import pandas as pd
import MySQLdb as md
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

prod_con_test  = md.connect(host='10.124.163.136', port=3306,user='root', passwd='root', db='woapp', charset="utf8")

def batch_sql(con, sql, param_list):    
    cur = con.cursor()
    print "sql=",sql
    print "param_list=", param_list
    reCout = cur.executemany(sql, param_list)
    print('data done size:{}'.format(reCout)) 
    con.commit()
    cur.close()
    return reCout

def importExcel():
    
    data = pd.read_excel('d:/tmp/renlian20180805.xlsx',header=None,encoding='utf-8')
    
    df = pd.DataFrame(data)
    df = df.loc[1:]
    
    sql = "insert  guest_num_day_copy (DAY_ID, STORE_ID, guest_num_all, guest_num_new, guest_num_old, guest_num_two,guest_num_men, guest_num_women,20_low, 20_29_in, 30_39_in,  40_49_in,  50_59_in, 60_up,  create_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    for index, row in df.iterrows():
        day_id = str(row[13])[0:10].replace('-','')   
        list_sql = []
        
        row[0] = row[0].replace(' ','')
        
        list_sql.append([day_id, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]])
        try:
            batch_sql(prod_con_test,sql,list_sql)
        except BaseException as ex:    
            print ex
            
if __name__ == '__main__':    
    importExcel()
    
    
    
    
    