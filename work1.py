
import time
import json
import requests
import pandas as pd
from openpyxl import load_workbook


def DateList(st, ed):
    format1 = '%Y%m%d'
    bgn = int(time.mktime(time.strptime(st, format1)))
    end = int(time.mktime(time.strptime(ed, format1)))
    list_date = [time.strftime(format1, time.localtime(i)) for i in range(bgn, end + 1, 3600 * 24)]
    return list_date
    pass


def Html_Data(url):
    response = requests.get(url=url, headers=header)
    if response.status_code == 200:
        data = response.content
        file = open("pig.html", "wb", 1)
        file.write(data)
        file.close()
        return data
        pass
    else:# 404 not found
        pass
    pass


def Get_Json(url):
    response = requests.get(url, headers=header)
    json_text = response.json()
    dump_data = json.dumps(json_text)
    load_data = json.loads(dump_data)
    # print(type(load_data), load_data)
    return load_data
    pass


def Get_Data(doc):
    dic = {}
    dic['pigprice'] = doc['pigprice']
    dic['pig_in'] = doc['pig_in']
    dic['pig_local'] = doc['pig_local']
    dic['maizeprice'] = doc['maizeprice']
    dic['bean'] = doc['bean']
    st = ''.join(doc['time'][3])
    ed = time.strftime('%Y%m%d', time.localtime(time.time()))
    # print(DateList(st, ed))
    dic['time'] = DateList(st, ed)
    return pd.DataFrame(dic)

#保存爬取的原始数据
def Save_Data(df):
    df.to_excel("原始数据.xlsx", index=False)
    wk = load_workbook("原始数据.xlsx")
    wb = wk["Sheet1"]
    wb.title = "价格数据"
    wk.save("原始数据.xlsx")
    pass


if __name__ == '__main__':
    html_url = 'https://zhujia.zhuwang.cc/api/chartData?areaId=-1&aa=1587965048621'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/8'}
    Html_Data(html_url)
    doc = Get_Json(html_url)
    df = Get_Data(doc)
    Save_Data(df)
    pass
