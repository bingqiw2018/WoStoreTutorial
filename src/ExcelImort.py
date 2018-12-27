#coding=utf-8 
'''
Created on 2018年5月24日

@author: bingqiw
'''
import pandas as pd

data = pd.read_excel('d:/tmp/201806130002.xlsx',header=None,encoding='utf-8')
print data.shape
df = pd.DataFrame(data)
name = 'd:/tmp/201806130003.xlsx'
df.to_excel(name,index=False,header=None)
print "end"