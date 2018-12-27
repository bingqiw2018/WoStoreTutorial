#coding=utf-8 
'''
Created on 2018年4月17日

@author: bingqiw
'''
import pandas as pd
import datetime

data = pd.read_table('d:/tmp/ESS_SaleInfo_20180407.txt',header=None,encoding='utf-8',sep=',')
df = pd.DataFrame(data)
df = df.loc[df[3] == 1]

name = 'd:/tmp/data_check'+datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')+'.xlsx'
df.to_excel(name,index=False,header=None)
print df.shape