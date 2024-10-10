import cv2
import fourierDescriptor as fd
import numpy as np

feature_path = 'E:/opencv/feature/'
img_path = 'E:/opencv/image/'
test_feature_path = 'E:/opencv/test_feature/'
test_img_path = 'E:/opencv/test_image/'
#'E./opencv/test_image/0_1.png'

if __name__ == "__main__":
    for i in range(1, 3):#0已经搞好了
        for j in range(1, 218):
            roi = cv2.imread(img_path + str(i) + '_' + str(j) + '.png')#读图片
            a,descirptor_in_use = np.abs(fd.fourierDesciptor(roi))#取特征矩阵
            fd_name = feature_path + str(i) + '_' + str(j) + '.txt'
            # fd_name = path + str(i) + '.txt'
            with open(fd_name, 'w', encoding='utf-8') as f:
                temp = descirptor_in_use[1]
                for k in range(1, len(descirptor_in_use)):
                    x_record = int(100 * descirptor_in_use[k] / temp)
                    f.write(str(x_record))
                    f.write(' ')
                f.write('\n')
            print('训练集', i, '_', j, '完成')

    for i in range(1, 3):#0已经搞好了
        for j in range(218, 223):
            roi = cv2.imread(test_img_path + str(i) + '_' + str(j) + '.png')#读图片
            a,descirptor_in_use = np.abs(fd.fourierDesciptor(roi))#取特征矩阵
            fd_name = test_feature_path + str(i) + '_' + str(j) + '.txt'
            # fd_name = path + str(i) + '.txt'
            with open(fd_name, 'w', encoding='utf-8') as f:
                temp = descirptor_in_use[1]
                for k in range(1, len(descirptor_in_use)):
                    x_record = int(100 * descirptor_in_use[k] / temp)
                    f.write(str(x_record))
                    f.write(' ')
                f.write('\n')
            print('测试集',  i, '_', j, '完成')

