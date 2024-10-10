import cv2
import picture as pic
import numpy as np
import fourierDescriptor as fd
import joblib
from SVM_train import *
import time

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体
size = 0.5  # 设置大小

width, height = 300, 300  # 设置拍摄窗口大小
x0, y0 = 100, 100  # 设置选取位置

cap = cv2.VideoCapture(0)  # 开摄像头

model_path = "E:/opencv/model/"
path = 'E:/opencv/new_image/'
path2 = 'E:/opencv/new_feature/'
i=0
a=0

if __name__ == "__main__":
    while (1):
        ret, frame = cap.read()  # 读取摄像头的内容
        # frame = cv2.flip(frame, 2)
        roi = pic.binaryMask(frame, x0, y0, width, height)  # 取手势所在框图并进行处理
        key = cv2.waitKey(1) & 0xFF  # 按键判断并进行一定的调整
        # 按'j''l''u''j'分别将选框左移，右移，上移，下移
        # 按'q'键退出录像
        if key == ord('i'):
            y0 += 5
        elif key == ord('k'):
            y0 -= 5
        elif key == ord('l'):
            x0 += 5
        elif key == ord('j'):
            x0 -= 5
        elif key == ord('y') :
            i = i+1
            # cv2.imwrite(path + str(i) + '.png', roi)
            # ret2, descirptor_in_use = np.abs(fd.fourierDesciptor(roi))
            # fd_name = path2 + str(i) + '.txt'
            # with open(fd_name, 'w', encoding='utf-8') as f:
            #     temp = descirptor_in_use[1]
            #     for k in range(1, len(descirptor_in_use)):
            #         x_record = int(100 * descirptor_in_use[k] / temp)
            #         f.write(str(x_record))
            #         f.write(' ')
            #     f.write('\n')
            print('图片', i, '完成')
            im=cv2.imread(str(i) + '.png')
            cv2.imshow(f'{i}',im)
            if cv2.waitKey(0)!=0:
                cv2.destroyWindow(f'{i}')
            # time.sleep(10)
            #
            # clf = joblib.load(model_path + "svm_efd_" + "train_model.m")
            # num = use_SVM(clf, 31, i)
        elif key == ord('q'):
            break
        cv2.imshow('frame', frame)  # 播放摄像头的内容
    cap.release()
    cv2.destroyAllWindows()  # 关闭所有窗口
