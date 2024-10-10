print("请输入：")
a=input()
b=input()
n=lena=len(a)
lenb=len(b)
print("被加/减数为：",a,lena)
print("加/减数为：",b,lenb)
l=1
if lena<lenb:
    a,b=b,a
    l=2
    n=lenb
elif lena==lenb:
    for i in range(lena):
        if a[i]>b[i]:
            break
        if a[i]<b[i]:
            a,b=b,a
            l=2
            break
b=b.zfill(n)
#加法
def add(x,y,c):
    z=x+y+c
    if(z>9):
        z=z-10
        c=1
    else : c=0
    return z,c
c=0
result=[]
for i in range(n-1,-1,-1): #加法结果保存
    d,c=add(int(a[i]),int(b[i]),c)
    result.append(d)
    if(i==0 and c==1):
        result.append(1)
n0=len(result)
for i in range(n0):   #列表倒序
    if(i==n0//2):break
    result[i],result[n0-1-i]=result[n0-1-i],result[i]

list=[str(i) for i in result]
result=''.join(list)
print("加法结果：",result,n0)

#减法
def sub(x,y,c):
    d=x-y-c
    if(d<0):
        d+=10
        c=1
    else:
        c=0
    return d,c
c=0
result1=[]
for i in range(n-1,-1,-1):
    d,c=sub(int(a[i]),int(b[i]),c)
    result1.append(d)
    if(i==0 and c==1):
        result1.append('-')
n1=len(result1)
p=0
for i in reversed(result1):
    if i==0:
        p+=1
    else:break

del result1[n1-p:n1]
n2=len(result1)
for i in range(n2):
    if (i == n2// 2): break
    result1[i], result1[n2 - 1 - i] = result1[n2 - 1 - i], result1[i]

list1=[str(i) for i in result1]
result1=''.join(list1)
if l==2:
    result1='-'+result1
print("减法结果：",result1,n2)