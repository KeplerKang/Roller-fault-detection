import numpy as np
from os import listdir
import joblib
from functools import reduce
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
#import matplotlib.pyplot as plt

feature_path = 'E:/opencv/feature/'
model_path = "E:/opencv/model/"
test_path = "E:/opencv/test_feature/"
new_feature_path = 'E:/opencv/new_feature/'

test_accuracy = []


# 读txt文件并将每个文件的描述子改为一维的矩阵存储
def txtToVector(filename, N):
    returnVec = np.zeros((1, N))
    fr = open(filename)
    lineStr = fr.readline()
    lineStr = lineStr.split(' ')
    for i in range(1, N):
        returnVec[0, i-1] = int(lineStr[i])
    return returnVec


def train_SVM(N):
    svc = SVC()
    parameters = {'kernel': ('linear', 'rbf'),
                  'C': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
                  'gamma': [0.00001, 0.0001, 0.001, 0.1, 1, 10, 100, 1000]}  # 预设置一些参数值
    hwLabels = []  # 存放类别标签
    trainingFileList = listdir(feature_path)
    m = len(trainingFileList)
    trainingMat = np.zeros((m, N))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        classNumber = int(fileNameStr.split('_')[0])
        hwLabels.append(classNumber)
        trainingMat[i, :] = txtToVector(feature_path + fileNameStr, N)  # 将训练集改为矩阵格式
    print("数据加载完成")
    clf = GridSearchCV(svc, parameters, cv=5, n_jobs=8)  # 网格搜索法，设置5-折交叉验证
    clf.fit(trainingMat, hwLabels)
    print(clf.return_train_score)
    print(clf.best_params_)  # 打印出最好的结果
    best_model = clf.best_estimator_
    print("SVM Model save...")
    save_path = model_path + "svm_efd_" + "train_model.m"
    joblib.dump(best_model, save_path)  # 保存最好的模型


def test_SVM(clf, N):
    testFileList = listdir(test_path)
    errorCount = 0  # 记录错误个数
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        classNum = int(fileNameStr.split('_')[0])
        vectorTest = txtToVector(test_path + fileNameStr, N)
        valTest = clf.predict(vectorTest)
        print("分类返回结果为%d\t真实结果为%d" % (valTest, classNum))
        if valTest != classNum:
            errorCount += 1
    print("总共错了%d个数据\n错误率为%f%%" % (errorCount, errorCount / mTest * 100))

def use_SVM(clf, N,i):
    testFileList = listdir(new_feature_path)
    fileNameStr = testFileList[i-1]
    vectorTest = txtToVector(new_feature_path + fileNameStr, N)
    valTest = clf.predict(vectorTest)
    print("手势识别为%d\t" % valTest)
    return valTest


####训练 + 验证#####
if __name__ == "__main__":
    train_SVM(31)
    clf = joblib.load(model_path + "svm_efd_" + "train_model.m")
    test_SVM(clf, 31)
