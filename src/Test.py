#coding=utf-8 
'''
Created on 2018年4月24日

@author: bingqiw
'''
import datetime
import time
import random
# ps.getImportStoreAddress("d:/tmp/address.xlsx")

# hb.getSaleInfoForAllProvice('2018', '05', 15)
# now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
# t = time.time()
# now_time = int(round(t * 1000))
#当前时间
def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - long(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp


while True:
    t = time.time()
    now_time = int(round(t * 1000 * 1000000)) + random.randint(0,1000000)
    print now_time
    














