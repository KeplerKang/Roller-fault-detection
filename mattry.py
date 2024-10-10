import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from math import sqrt
from sklearn.metrics import mean_squared_error
from matplotlib import rcParams
rcParams['font.family'] = rcParams['font.sans-serif'] = 'SimHei'
pd.set_option('display.unicode.east_asian_width',True)
import pmdarima as pm
from pmdarima import auto_arima
dt  = pd.read_excel("E:\pythonProject\附件2：节点实时电价.xlsx",sheet_name=['15分钟'])
df = dt['15分钟']
table = df.values
X1=range(table.shape[0]*24*4)
Y1=table[:,1:].flatten()
train = DataFrame(Y1[:2016].reshape((2016, 1)), index=range(1,2017))
valid = DataFrame(Y1[2016:].reshape((864, 1)), index=range(2017,2881))
# print(data.drop([0,1]))

model = auto_arima(train, trace=True, error_action='ignore', suppress_warnings=True)
model.fit(train)

forecast = model.predict(n_periods=len(valid))
forecast = pd.DataFrame(forecast,index = valid.index,columns=['Prediction'])

#plot the predictions for validation set
plt.plot(train, label='Train',color='blue')
plt.plot(valid, label='Valid',color='green')
plt.plot(forecast, label='Prediction',color='red')
rms = sqrt(mean_squared_error(valid,forecast))
plt.show()
print(rms)

'''
dt  = pd.read_excel("E:\pythonProject\附件2：节点实时电价.xlsx",sheet_name=['15分钟',0])
df = dt['15分钟']
table = df.values
X1=range(table.shape[0]*24*4)
Y1=table[:,1:].flatten()
#ax= plt.figure().add_subplot()
#ax.plot(X1,Y1)

dt2  = pd.read_excel("E:\pythonProject\附件4：备用信息值.xlsx",sheet_name=['备用信息实际值',0])
df2 = dt2['备用信息实际值']
table2 = df2.values
X2=range((table2.shape[0]-1)*24*4)
Y2=table2[1:,1::2].flatten()
#ax= plt.figure().add_subplot()
#ax.plot(X2,Y2)

dt3  = pd.read_excel("E:\pythonProject\附件4：备用信息值.xlsx",sheet_name=['备用信息实际值',0])
df3 = dt3['备用信息实际值']
table3 = df3.values
X3=range((table3.shape[0]-1)*24*4)
Y3=table3[1:,2::2].flatten()
#ax= plt.figure().add_subplot()
#ax.plot(X3,Y3)

dt4 = pd.read_excel("E:\pythonProject\附件3：实际负荷信息.xlsx",sheet_name=['Sheet1',0])
df4 = dt4['Sheet1']
table4= df4.values
X4=range(table4.shape[0]*24*4)
y4=table4[:,1:-1].flatten()
Y4=[i/100 for i in y4]

plt.figure(num='各时间节点下，电价与实际负荷折线图')
plt.plot(X1,Y1)
plt.plot(X4,Y4)
'''
