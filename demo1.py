# pdf转excel
import pdfplumber
import xlwt

path = "E:/2019srbook.pdf"
#path = "aaaaaa.PDF"  # 导入PDF路径
pdf = pdfplumber.open(path)
print('\n')
print('开始读取数据')
print('\n')

for page in pdf.pages:
    if page.page_number==14:
        now=page

# 获取当前页面的全部文本信息，包括表格中的文字，复制粘贴到txt里!!!!!!!!!!!
# print(now.extract_text())
#从txt里读取成列表的形式
all=[]
fr = open('E:/drf.txt',encoding='utf-8')
for line in fr.readlines():
    lineArr = line.split(' ')
    a=[]
    for j in range(len(lineArr)):
        a.append(lineArr[j])
    all.append(a)

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('Sheet1')
for i in range(len(all)):
    for j in range(len(all[0])):
        worksheet.write(i+1,j, label = all[i][j])

# 保存
workbook.save('E:/Page12.xls')
print('\n')
print('写入excel成功')