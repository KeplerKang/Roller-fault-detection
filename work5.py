
import pandas as pd
from pandas import read_excel
import matplotlib.pyplot as plt
import matplotlib.dates as mdate


def Anlys(df):
    data1 = df[0:][['预测', '实际']]
    data2 = data1.T
    data2.loc["标准差"] = data2.apply(lambda x: x.std())
    data2.loc["方差"] = data1.T.apply(lambda x: x.var())
    data2.to_excel("误差分析.xlsx", index=True)
    pass


def Fig(df1):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

    data = read_excel('误差分析.xlsx').T
    data.to_excel("误差分析1.xlsx", index=False, columns=None)
    data1 = read_excel('误差分析1.xlsx')
    data1.rename(columns={0: '预测', 1: '实际', 2: '标准差', 3: '方差'}, inplace=True)
    data2 = data1.drop(index=[0])
    plt.rcParams['axes.unicode_minus']
    x1 = df1['日期']
    y1 = data2['预测']
    y2 = data2['实际']
    y3 = data2['标准差']
    y4 = data2['方差']
    plt.figure()
    plt.plot(x1, y1, 'r', linestyle="--",linewidth=1)
    plt.plot(x1, y2, 'b', linestyle="--",linewidth=1)
    plt.title('预测价格与实际价格波动情况', fontsize=10)
    plt.xlabel('日期')
    plt.ylabel('生猪价格(元/公斤)')
    plt.legend(['预测价格','实际价格'])
    plt.figure()
    ax1 = plt.subplot(211)
    plt.title('标准差与日期')
    plt.plot(x1, y3, color="g", linestyle="--",linewidth=1)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    plt.xticks([])
    plt.xlabel("日期")
    # plt.grid(True)
    ax2 = plt.subplot(212)
    plt.title('方差与日期')
    plt.plot(x1, y4, color="y", linestyle="--",linewidth=1)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    plt.xticks([])
    plt.ylabel("方差")
    plt.xlabel("日期")
    plt.show()
    pass


if __name__ == '__main__':
    data1 = pd.read_excel('预测数据.xlsx')
    data2 = read_excel('预处理2.xlsx')
    Anlys(data1)
    Fig(data2)
    pass
