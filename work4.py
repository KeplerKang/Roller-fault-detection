
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_excel('预处理1.xlsx')
data = df[0:][['玉米', '豆粕', '生猪']]
data.to_excel("预处理3.xlsx", index=False)
data = pd.read_excel('预处理3.xlsx')
data = data.values.copy()

# 计算互相关系数，参数为预报因子序列及滞时k
def get_regre_coef(X, Y, k):
    S_xy = 0
    S_xx = 0
    S_yy = 0
    X_mean = np.mean(X)
    Y_mean = np.mean(Y)
    for i in range(len(X) - k):
        S_xy += (X[i] - X_mean) * (Y[i + k] - Y_mean)
    for i in range(len(X)):
        S_xx += pow(X[i] - X_mean, 2)
        S_yy += pow(Y[i] - Y_mean, 2)
    return S_xy / pow(S_xx * S_yy, 0.5)


# 计算三种商品两两之间互相关系数
def regre_coef_matrix(data):
    row = data.shape[1]
    r_matrix = np.ones((1, row - 2))
    for i in range(1, row - 1):
        r_matrix[0, i - 1] = get_regre_coef(data[:, i], data[:, row - 1], 1)# 这里表示滞时为1天
    return r_matrix


r_matrix = regre_coef_matrix(data)


def get_menxiannum(r_matrix):
    row = r_matrix.shape[1]
    for i in range(row):
        if r_matrix.max() == r_matrix[0, i]:
            return i + 1
    return -1


m = get_menxiannum(r_matrix)


def resort_bymenxian(data, m):
    data = data.tolist()
    data.sort(key=lambda x: x[m])
    data = np.array(data)
    return data


data = resort_bymenxian(data, m)

def get_var(x):
    return x.std() ** 2 * x.size


def get_F(Y):
    col = Y.shape[0]
    FF = np.ones((1, col - 1))
    V = get_var(Y)
    for i in range(1, col):
        S = get_var(Y[0:i]) + get_var(Y[i:col])
        F = (V - S) * (col - 2) / S
        FF[0, i - 1] = F
    return FF


y = data[:, data.shape[1] - 1]
FF = get_F(y)


def get_index(FF, element):
    i = -1
    for item in FF.flat:
        i += 1
        if item == element:
            return i


f_index = get_index(FF, np.max(FF))


def data_excision(data, f_index):
    f_index = f_index + 1
    data1 = data[0:f_index, :]
    data2 = data[f_index:data.shape[0], :]
    return data1, data2


data1, data2 = data_excision(data, f_index)


def get_XY(data):
    Y = data[:, data.shape[1] - 1]
    X = data[:, 1:data.shape[1] - 1]
    return X,Y


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
X, Y = get_XY(data1)
regs = LinearRegression()
regs.fit(X, Y)
Y1 = regs.predict(X)
X, Y = get_XY(data2)
regs.fit(X, Y)
Y2 = regs.predict(X)
Y = np.column_stack((data[:, 0], np.hstack((Y1, Y2)))).copy()
Y = np.column_stack((Y, data[:, data.shape[1] - 1]))
Y = resort_bymenxian(Y, 0)
Y = resort_bymenxian(Y, 0)
pdt = pd.DataFrame(Y)
pdt.rename(columns={0: '玉米', 1: '预测', 2: '实际'}, inplace=True)
pdt.to_excel("预测数据.xlsx", index=False)
plt.rcParams['axes.unicode_minus']
ax1 = plt.subplot(211)
plt.plot(Y[:, 0], Y[:, 1], 'r', linestyle="--",linewidth=1)
plt.xlabel('玉米价格')
plt.ylabel('生猪价格')
ax1 = plt.subplot(212)
plt.plot(Y[:, 0], Y[:, 2], 'blue', linestyle="--",linewidth=1)
plt.title('实际值', fontsize=10)
plt.xlabel('玉米价格')
plt.ylabel('生猪价格')
plt.figure()
plt.plot(Y[:, 0], Y[:, 1]-Y[:, 2], 'g', linestyle="--",linewidth=1)
# plt.plot(Y[:, 0], Y[:, 2], 'g', linestyle="-")
plt.title('玉米价格与生猪价格门限回归分析', fontsize=10)
plt.xlabel('玉米价格(元/吨)')
plt.ylabel('生猪价格(元/公斤)')
plt.legend(['预测-实际'])
plt.show()