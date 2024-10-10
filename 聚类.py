all=[(2,5),(2,10),(8,4),(5,8),(4,9)]
print(all)
m1=all[0];m2=all[4]#初始化簇中心
print('初始中心为：'+str(m1)+'和'+str(m2))

def julei(x,y):
    c = []
    d = []
    for i in all:
        a=(i[0]-x[0])**2+(i[1]-x[1])**2
        b=(i[0]-y[0])**2+(i[1]-y[1])**2
        if(a<=b):
            c.append(i)
        else:
            d.append(i)
        #按旧的中心聚类
    sum1=sum2=0
    for j in c:
        sum1 += j[0]
        sum2 += j[1]
    sum1 = sum1 / len(c)
    sum2 = sum2 / len(c)
    x1=(sum1,sum2)#新的m1中心
    sum3 = sum4 = 0
    for j in d:
        sum3 += j[0]
        sum4 += j[1]
    sum3 = sum3 / len(d)
    sum4 = sum4 / len(d)
    y1=(sum3,sum4)#新的m2中心
    sign=0
    if(x==x1 and y==y1):
        sign=1
        print(c,d)
    else:
        print('迭代后簇中心为：' + str(x1) + '和' +str(y1))
    return x1,y1,sign

while(1):
    m1,m2,s=julei(m1,m2)
    if s==1:
        print('迭代完成')
        break
