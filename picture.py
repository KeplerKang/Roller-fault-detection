import cv2
import numpy as np
import fourierDescriptor as fd

# #以3*3的模板进行均值滤波
# blur = cv2.blur(roi, (3,3))
# #以3*3的模板进行高斯滤波，最后一个参数表示x与y方向的标准差，给0的话，函数会自己运算
# blur = cv2.GaussianBlur(roi, (3,3), 0)
# #中值滤波
# blur = cv2.medianBlur(roi,5)
# #双边滤波，9为区域的直径，后面两个参数是空间高斯函数标准差和灰度值相似性高斯函数标准差
# blur = cv2.bilateralFilter(img,9,75,75)

def binaryMask(frame, x0, y0, width, height):
    cv2.rectangle(frame, (x0, y0), (x0 + width, y0 + height), (0, 255, 0))  # 画出截取的手势框图
    roi = frame[y0:y0 + height, x0:x0 + width]  # 获取手势框图
    # cv2.imshow("roi", roi)  # 显示手势框图
    res = skinMask(roi)  # 进行肤色检测
    #cv2.imshow("res", res)  # 显示肤色检测后的图像
    # 形态学处理，去除白点和黑点
    # kernel = np.ones((3, 3), np.uint8)  # 设置卷积核
    # erosion = cv2.erode(res, kernel)  # 腐蚀操作
    #cv2.imshow("erosion", erosion)
    # dilation = cv2.dilate(erosion, kernel)  # 膨胀操作
    #cv2.imshow("dilation", dilation)
    # 傅里叶算子提取
    # ret, fourier_result = fd.fourierDesciptor(res)
    #截短后重建的 res =fd.reconstruct(ret,fourier_result)
    #手势轮廓提取，这里使用后面的傅里叶算子
    # binaryimg = cv2.Canny(res, 50, 200)  # 二值化，canny检测
    # contoursh,b= cv2.findContours(binaryimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓 # 提取轮廓
    # ret = np.ones(res.shape, np.uint8)  # 创建黑色幕布
    # cv2.drawContours(ret, contours, -1, (255, 255, 255), 1)  # 绘制白色轮廓
    # cv2.imshow("ret", ret)
    return roi


##########方法一###################
##########BGR空间的手势识别#########
def skinMask(roi):
    rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)  # 转换到RGB空间
    (R, G, B) = cv2.split(rgb)  # 获取图像每个像素点的RGB的值，即将一个二维矩阵拆成三个二维矩阵
    skin = np.zeros(R.shape, dtype=np.uint8)  # 掩膜
    (x, y) = R.shape  # 获取图像的像素点的坐标范围
    for i in range(0, x):
        for j in range(0, y):
            # 判断条件，不在肤色范围内则将掩膜设为黑色，即255
            if (abs(R[i][j] - G[i][j]) > 15) and (R[i][j] > G[i][j]) and (R[i][j] > B[i][j]):
                if (R[i][j] > 95) and (G[i][j] > 40) and (B[i][j] > 20) \
                        and (max(R[i][j], G[i][j], B[i][j]) - min(R[i][j], G[i][j], B[i][j]) > 15):
                    skin[i][j] = 255
                elif (R[i][j] > 220) and (G[i][j] > 210) and (B[i][j] > 170):
                    skin[i][j] = 255
    res = cv2.bitwise_and(roi, roi, mask=skin)  # 图像与运算
    return res

