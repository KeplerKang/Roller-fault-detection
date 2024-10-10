
import pandas as pd
from pandas import read_excel
import matplotlib.pyplot as plt
import matplotlib.dates as mdate


def analysis(data):
    data1 = data[0:][['pigprice', 'pig_in', 'pig_local']]
    data1['pig_mean'] = data1.apply(lambda x: x.mean(), axis=1)
    data1['pig_mean'] = data1['pig_mean'].map(lambda x: x / 1)
    data1['pig_mean'] = round(data1['pig_mean'], 2)
    data2 = data[0:][['maizeprice', 'bean', 'time']]
    data2['pig_mean'] = data1[0:][['pig_mean']]
    columns = ['time', 'pig_mean', 'maizeprice', 'bean']
    data2 = pd.DataFrame(data2, columns=columns)
    data2.rename(columns={'time': '日期',
                          'pig_mean': '生猪',
                          'maizeprice': '玉米',
                          'bean': '豆粕'}, inplace=True)
    data2.to_excel("预处理1.xlsx", index=False)
    data2['日期'] = pd.to_datetime(data2['日期'], format='%Y%m%d')
    data2.to_excel("预处理2.xlsx", index=False)
    pass


def Fig(data):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

    fig = plt.figure()
    x = data['日期']
    y1 = data['生猪']
    y2 = data['玉米']
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1, 'r-')
    ax1.set_ylabel("生猪平均价格(元/公斤)")
    ax1.set_title("生猪价格与玉米价格波动情况")
    plt.xticks([])
    plt.legend(['生猪价格'],loc='upper left')
    ax2 = ax1.twinx()
    ax2.plot(x, y2, 'b-')
    ax2.set_ylabel('玉米(15%水分) 元/吨')
    ax2 = plt.gca()
    ax2.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    plt.xticks([])
    # print(pd.date_range('2020-11-11', '2021-11-10', freq='1m'))
    plt.legend(['玉米价格'])

    plt.figure()
    plt.title('生猪价格与日期')
    plt.plot(data['日期'], data['生猪'], color="r", linestyle="-")
    b = data['生猪'].argmax()
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    plt.xticks([])
    plt.annotate(data['生猪'][b], xy=(data['日期'][b], 41),
                 xytext=(data['日期'][100], 35),
                 arrowprops=dict(facecolor='r', shrink=0.1, width=0.5))
    plt.ylabel("生猪平均价格(元/公斤)")
    plt.xlabel("日期")

    plt.figure()
    plt.title('玉米价格与日期')
    plt.plot(data['日期'], data['玉米'], color="b", linestyle="-")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    plt.xticks([])
    plt.ylabel("玉米(15%水分) 元/吨")
    plt.xlabel("日期")
    # plt.grid(True)
    plt.figure()
    plt.title('豆粕价格与日期')
    plt.plot(data['日期'], data['豆粕'], color="g", linestyle="-")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    plt.xticks([])
    plt.ylabel("豆粕(43%蛋白) 元/吨")
    plt.xlabel("日期")

    plt.show()
    pass


if __name__ == '__main__':
    df = read_excel('原始数据.xlsx')
    analysis(df)
    data = pd.read_excel('预处理2.xlsx')
    Fig(data)
    pass
