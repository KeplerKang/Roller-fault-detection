
import matplotlib
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def analysis1(data):
    plt.rcParams['axes.unicode_minus']
    x = data[['玉米']]
    y = data[['生猪']]
    plt.figure()
    plt.scatter(data.玉米, data.生猪)
    plt.title('生猪价格与玉米价格')
    plt.xlabel('玉米价格')
    plt.ylabel('生猪价格')
    plt.grid(True)
    plt.plot(x, y, 'k.')
    plt.show()
    pass


def analysis2(data):
    font = {'family': 'SimHei'}
    matplotlib.rc('font', **font)
    matplotlib.rcParams['axes.unicode_minus'] = False
    scatter_matrix(data[["生猪", "玉米"]],
                   alpha=0.8, figsize=(10, 10), diagonal='kde')
    pass


def analysis3(data):
    plt.rcParams['axes.unicode_minus']
    x = data[['玉米']]
    y = data[['生猪']]
    pf = PolynomialFeatures(degree=2)
    x_2_fit = pf.fit_transform(x)
    x_2_predict = pf.fit_transform([[1990], [2000], [2010]])
    # print(x_2_fit)
    lrModel = LinearRegression()
    print(type(x))
    a=lrModel.fit(x_2_fit, y)
    b=lrModel.score(x_2_fit, y)
    c=lrModel.predict(x_2_predict)
    print(a,b,c)
    pass


if __name__ == '__main__':
    data = pd.read_excel('预处理1.xlsx')
    analysis1(data)
    analysis2(data)
    analysis3(data)
    pass
