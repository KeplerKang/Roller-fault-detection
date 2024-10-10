import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = rcParams['font.sans-serif'] = 'SimHei'

pd.set_option('display.unicode.east_asian_width',True)
dt  = pd.read_excel("E:\pythonProject\\avg_on_weekdays.xlsx",sheet_name=['Sheet1',0])
df = dt['Sheet1']

table = df.values
X1=range(table.shape[0]*24)
Y1=table[:,1:-2].flatten()
ax= plt.figure().add_subplot()
ax.plot(X1,Y1)

dt2  = pd.read_excel("E:\pythonProject\\avg_on_weekends.xlsx",sheet_name=['Sheet1',0])
df2 = dt2['Sheet1']
table2 = df2.values
X2 = range(table2.shape[0]*24)
Y2 = table2[:,1:-2].flatten()
ax = plt.figure().add_subplot()
ax.plot(X2,Y2)

table3 = df.values
list3 = table3.tolist()
list_del = []
tmp = table3[0][-1]
for i in range(table3.shape[0]):
    if(abs(list3[i][-1]-tmp)>5):
        list_del.append(list3[i][0])
        list3[i][0]='0'
    else:
        tmp = list3[i][-1]
df3 = pd.DataFrame(data = list3,columns= df.columns)
df3.set_index('日期',inplace = True)
df3.drop('0',inplace=True)
table3 = df3.values
# print(table3.shape)
X3 = range(table3.shape[0]*24)
Y3 = table3[:,0:-2].flatten()
# print(len(X3))
# print(Y3.shape)
ax = plt.figure().add_subplot()
ax.plot(X3,Y3)
plt.show()
# chunjieWD = ['2020-01-24','2020-01-27','2020-01-28','2020-01-29','2020-01-30','2020-01-31']
# chunjieWE = ['2020-01-25','2020-01-26','2020-02-01','2020-02-02']
# guoqingWD = ['2020-10-01','2020-10-02','2020-10-05','2020-10-06','2020-10-07']
# guoqingWE = ['2020-10-03','2020-10-04']

# df3 = df.set_index('日期')
# df3.drop(chunjieWD+guoqingWD,axis = 0,inplace=True)
# df4 = df2.set_index('日期')
# df4.drop(chunjieWE+guoqingWE,axis = 0,inplace=True)
# table3 = df3.values
# print(table3.shape)
# X3 = range(table3.shape[0]*24)
# Y3 = table3[:,0:-2].flatten()
# ax = plt.figure().add_subplot()
# ax.plot(X3,Y3)

# table4 = df4.values
# X4 = range(table4.shape[0]*24)
# Y4 = table4[:,0:-2].flatten()
# ax = plt.figure().add_subplot()
# ax.plot(X4,Y4)
