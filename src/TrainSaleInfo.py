#coding=utf-8 
'''
Created on 2018年3月29日

@author: bingqiw
'''
import numpy as np
import pandas as pd
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt

data_src = pd.read_excel('D:/Program Files/eclipse4.6/workspace/WoStore/data/train_wostore_sales_1000.xlsx',header=None,encoding='utf-8')
# print data_src.head()
data0 = data_src.loc[:,[1,6,7]]
data1 = data_src.loc[:,[1,7]]
target = data_src.loc[:,8]
# print "============================="
# print data0.shape[0]
# print target.shape

def plot_line(data, target):
    num = np.arange(0.1,0.8,0.05)
    size = np.zeros(len(num))
    train_arr = np.zeros(len(num))
    test_arr = np.zeros(len(num))
    pre_list = []
    count = 0
#     print "start ------------------------------------"
    for index in num:
        X_train, X_test, y_train, y_test = train_test_split(data, target,train_size=index, test_size=0.20, random_state=0)
        cls = LogisticRegression()
        cls.fit(X_train, y_train)
        train_score = cls.score(X_train, y_train)
        test_score = cls.score(X_test,y_test)
        pre_score = cls.predict(X_test)
        tmp_df = pd.DataFrame(X_test)
        tmp_df[9] = pre_score
        tmp_df = tmp_df.loc[tmp_df[9] == 1]
#         print tmp_df
        pre_list.append(tmp_df)
#         print tmp_df.shape
        if count < len(num):
            size[count] = data.shape[0]*index 
            train_arr[count] = train_score
            test_arr[count] = test_score
#             pre_arr[count] = pre_score
#             print('exp:{0};train:{1};test{2}'.format(size[count],train_score,test_score)) 
        count = count + 1
#     print "end ------------------------------------"
    return train_arr,test_arr, pre_list, size

def plot_train(size, arr, label_text, line_color):
    plt.plot(size,arr, 'o',label= label_text, color= line_color , linewidth=2.0, linestyle="-")

def get_predict_result(pre_list):
    df = pd.concat(pre_list)
    df = df.groupby(by=[7])[9].sum()
    df = pd.DataFrame(df).sort_values(by=9 ,ascending=False) 
    print "预测结果："
    name = 'd:/tmp/pred'+datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')+'.xlsx'
    df.to_excel(name)
    print df
        
train_arr, test_arr, pre_list, size = plot_line(data0, target);  
plot_train(size,train_arr, u"改进训练","blue" )
plot_train(size,test_arr, u"改进测试","red" )
# get_predict_result(pre_list)
train_arr, test_arr, pre_list, size = plot_line(data1, target);   
plot_train(size,train_arr, u"欠拟合","green" )

plt.legend(loc = 0) #设置legend
plt.grid()
plt.ylim(0.7,1.0)
plt.xlim(100,750)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.ylabel(u"准确率")
plt.xlabel(u"训练集大小")
plt.show() 

# print('train_score:{0:.2f}; test_score:{1:.2f};'.format(train_score,test_score)) 







