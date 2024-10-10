import copy
box={'A':6,'B':6,'C':4,'D':4,'E':4,'F':4,'G':4,'H':3,'I':3}
allcase=[]
for x in box:
    p1 = box[x]/sum(box.values())
    box1 = copy.deepcopy(box)
    box1.pop(x)
    for y in box1:
        p2 = box1[y] / sum(box1.values())
        box2 = copy.deepcopy(box1)
        box2.pop(y)
        for z in box2:
            p3 = box2[z] / sum(box2.values())
            box3 = copy.deepcopy(box2)
            box3.pop(z)
            for w in box3:
                p4 = box3[w] / sum(box3.values())
                p=p1*p2*p3*p4
                allcase.append([x,y,z,w,p])
pp=0
for t in allcase:
    if 'H' in t and 'I' in t:
        pp+=t[4]
print(pp)

