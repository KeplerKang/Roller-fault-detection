# import time
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# from openpyxl import load_workbook
#
#
# if __name__ == '__main__':
#     html_url = "https://xy2.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search_equip"
#     header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                             'Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/8'}
#     res = requests.get(url=html_url,headers=header)
#     res.encoding='gbk'
#     # print(res.text)
#     bs = BeautifulSoup(html_url,"html.parser")
#     print(bs.name)


# df = pd.read_csv('https://archive.ics.uci.edu/ml/'
#                  'machine-learning-databases/iris/iris.data', header=None)
# y = df.iloc[0:100, 0].values
# print(max(y))
# plt.scatter(x[:50,0],x[:50,1],color='red',marker='o',label='setosa')
# plt.scatter(x[50:100,0],x[50:100,1],color='blue',marker='x',label='setosa')
# plt.xlabel('petal length')
# plt.ylabel('sepal length')
# plt.legend(loc='upper left')
# plt.show()
# w = [0.9, 0.6, 1.25]
# for i in range(8):
#     x = df.iloc[0:100,0].values

# print(self.w)
# b = -self.w[0] / self.w[2] - self.w[1] * a / self.w[2]
# plt.plot(a, b, color='green', linewidth=1.0, linestyle='-')
# plt.scatter(er[:,0], er[:,1], color='red', marker='o', label='setosa')
# plt.scatter(x[:50, 0], x[:50, 1], color='red', marker='o', label='setosa')
# plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', label='setosa')
# plt.xlabel('petal length')
# plt.ylabel('sepal length')
# plt.legend(loc='upper left')
# plt.pause(5)
# plt.cla()

# plt.ion()
# plt.ioff()

# df = pd.read_csv('https://archive.ics.uci.edu/ml/'
#                  'machine-learning-databases/iris/iris.data', header=None)

# fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
# ax[0][0].plot(range(5), range(0, 10, 2), marker='o')
# ax[1,1].plot(range(2, 8), range(2, 18, 3), marker='x')
# plt.show()

