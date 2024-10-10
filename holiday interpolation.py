# coding:utf-8
import pandas as pd
from pandas import DataFrame

# 读取文件
data = pd.read_excel("C:/Users/Lenovo/Desktop/gold.xlsx", sheet_name="Sheet1")
for i in range(1824):
    if data['preGzf'][i] == 0:
        data['10bias'][i] = 0
DataFrame(data).to_excel('C:/Users/Lenovo/Desktop/gold.xlsx', sheet_name='Sheet1', index=False, header=True)
