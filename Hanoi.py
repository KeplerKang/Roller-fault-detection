# def move(m,x,y):
#     print('将',m,'号盘从',x,'移动到',y)
#
# def hanoi(n,A,B,C):
#     if n==1:
#         move(1,A,C)
#     else:
#         hanoi(n-1,A,C,B)
#         move(n,A,C)
#         hanoi(n-1,B,A,C)
#
# if __name__ == '__main__':
#     n=int(input('请输入汉诺塔盘子数:\n'))
#     print(type(n))
#     hanoi(n,'o','p','q')

import turtle
class Stack:  #面向对象，定义一个类
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
def drawpole_3():
    t = turtle.Turtle()
    def drawpole_1(k):
        t.up()
        t.pensize(10)
        t.speed(100)
        t.goto(400*(k-1), 300)
        t.down()
        t.goto(400*(k-1), -100)
    drawpole_1(0)
    drawpole_1(1)
    drawpole_1(2)
def creat_plates(n): #按照输入的n来画出盘子个数
    plates=[turtle.Turtle() for i in range(n)]
    for i in range(n):
        plates[i].up()
        plates[i].shape("square")
        plates[i].shapesize(1,20-i)
        plates[i].goto(-400,-90+20*i)
        plates[i].showturtle()
    return plates
def pole_stack(): #这里运用栈来控制一次只能搬动一个盘子并且递归
    poles=[Stack() for i in range(3)]
    return poles
def moveDisk(plates,poles,fp,tp): #搬动盘子
    mov=poles[fp].peek()
    plates[mov].goto((fp-1)*400,300)
    plates[mov].goto((tp-1)*400,300)
    l=poles[tp].size()
    plates[mov].goto((tp-1)*400,-90+20*l)
def moveTower(plates,poles,height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(plates,poles,height-1,fromPole,withPole,toPole)
        moveDisk(plates,poles,fromPole,toPole)
        poles[toPole].push(poles[fromPole].pop())
        moveTower(plates,poles,height-1,withPole,toPole,fromPole)

n=int(input("请输入汉诺塔的层数并回车:\n"))
myscreen=turtle.Screen()
myscreen.setup(1700,800)
drawpole_3()
plates=creat_plates(n)
poles=pole_stack()
for i in range(n):
    poles[0].push(i)
moveTower(plates,poles,n,0,2,1)
myscreen.exitonclick()
