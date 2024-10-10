safe = [(0, 0, 0), (0, 1, 1), (0, 1, 0), (0, 2, 1), (0, 2, 0), (0, 3, 1), (1, 1, 1), (1, 1, 0), (2, 2, 1), (2, 2, 0),
        (3, 0, 0), (3, 1, 1), (3, 1, 0), (3, 2, 1), (3, 2, 0), (3, 3, 1)]#合法且安全的状态
action = [(1, 0), (1, 1), (2, 0), (0, 1), (0, 2)]#可执行的操作
old = [(3, 3, 1, "3,3,1")]#初始化
time = 0
def mc(old,time):#通过迭代寻找可行路径
        new = []
        state = [0, 0, 0, ""]#第四个量用来存储路径
        finish = False
        for old_s in old:
                for act in action:
                        if old_s[2] == 1:#往右走
                                for i in range(2):
                                        state[i] = old_s[i]-act[i]#左岸人减少
                                state[2] = 0#船到右岸
                                state[3] = old_s[3]+f"->{state[0]},{state[1]},{state[2]}"#跟新路径
                        else:#往左走
                                for i in range(2):
                                        state[i] = old_s[i] + act[i]#右岸人减少
                                state[2] = 1
                                state[3] = old_s[3] + f"->{state[0]},{state[1]},{state[2]}"#跟新路径
                        if tuple(state[0:3]) in safe:
                                new.append(state[:])#将结果中合法的状态添加到数组中
        for state in new:
                if state[:3] ==[0, 0, 0]:
                        finish = True
                        print(state[3])
        if finish == True:
                print(f"最短步骤数为:{time+1}")
        if finish == False:
                mc(new, time+1)
mc(old,0)
