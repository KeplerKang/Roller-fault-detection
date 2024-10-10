# import requests
# from bs4 import BeautifulSoup
#
# resp=requests.get('https://www.cctv.com/')
# print(resp)
# bsobj=BeautifulSoup(resp.content,'lxml')
# a_list=bsobj.find_all('a') #获取网页中的所有a标签对象
# for a in a_list:
#     print(a.get('href')) #打印

import csv
with open('1.csv', encoding='utf-8-sig') as f:
    cnt=0
    for row in csv.reader(f, skipinitialspace=True):
        if row[0]=='上海虹桥昆山南':
            cnt+=1
    print(cnt)


