import time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

def distEclud(vecA,vecB):
    """
    计算两个向量的欧式距离
    """
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))

def randCent(dataSet,k):
    """
    随机生成k个点作为质心，其中质心均在整个数据数据的边界之内
    """
    n=dataSet.shape[1] # 获取数据的维度
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = np.min(dataSet[:,j])
        rangeJ = np.float(np.max(dataSet[:,j])-minJ)
        centroids[:,j] = minJ+rangeJ*np.random.rand(k,1)
    return centroids

def kMeans(dataSet,k,distMeas=distEclud, createCent=randCent):
    """
    k-Means聚类算法,返回最终的k各质心和点的分配结果
    """
    m = dataSet.shape[0]  #获取样本数量
    # 构建一个簇分配结果矩阵，共两列，第一列为样本所属的簇类值，第二列为样本到簇质心的误差
    clusterAssment = np.mat(np.zeros((m,2)))
    # 1. 初始化k个质心
    centroids = createCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1
            # 2. 找出最近的质心
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            # 3. 更新每一行样本所属的簇
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:]=minIndex,minDist**2
        print(centroids) # 打印质心
        # 4. 更新质心
        for cent in range(k):
            ptsClust = dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]] # 获取给定簇的所有点
            centroids[cent,:] = np.mean(ptsClust,axis=0) # 沿矩阵列的方向求均值
    return centroids,clusterAssment

def biKmeans(dataSet, k, distMeas=distEclud):
    """
    二分k-Means聚类算法,返回最终的k各质心和点的分配结果
    """
    m = dataSet.shape[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    # 创建初始簇质心
    centroid0 = np.mean(dataSet,axis=0).tolist()[0]
    centList = [centroid0]
    # 计算每个点到质心的误差值
    for j in range(m):
        clusterAssment[j,1] = distMeas(np.mat(centroid0),dataSet[j,:])**2
    while (len(centList) < k):
        lowestSSE = np.inf
        for i in range(len(centList)):
            # 获取当前簇的所有数据
            ptsInCurrCluster = dataSet[np.nonzero(clusterAssment[:,0].A == i)[0],:]
            # 对该簇的数据进行K-Means聚类
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster,2,distMeas)
            sseSplit = sum(splitClustAss[:,1]) # 该簇聚类后的sse
            sseNotSplit = sum(clusterAssment[np.nonzero(clusterAssment[:,0].A != i)[0],1]) # 获取剩余收据集的sse
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        # 将簇编号0,1更新为划分簇和新加入簇的编号
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 1)[0],0]= len(centList)
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 0)[0],0]= bestCentToSplit

        print("the bestCentToSplit is: ",bestCentToSplit)
        print("the len of bestClustAss is: ",len(bestClustAss))
        # 增加质心
        centList[bestCentToSplit] = bestNewCents[0,:]
        centList.append(bestNewCents[1,:])

        # 更新簇的分配结果
        clusterAssment[np.nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:] = bestClustAss
    return centList, clusterAssment

def load_data_make_blobs():
    """
    生成模拟数据
    """
    from sklearn.datasets import make_blobs  # 导入产生模拟数据的方法
    k = 5  # 给定聚类数量
    X, Y = make_blobs(n_samples=1000, n_features=2, centers=k, random_state=1)
    return X,k

if __name__ == '__main__':
    X, k=load_data_make_blobs()  # 获取模拟数据和聚类数量
    s = time.time()
    myCentroids, clustAssing = biKmeans(X, k)  # myCentroids为簇质心
    print("用二分K-Means算法原理聚类耗时：", time.time() - s)
    centroids = np.array([i.A.tolist()[0] for i in myCentroids])  # 将matrix转换为ndarray类型
    # 获取聚类后的样本所属的簇值，将matrix转换为ndarray
    y_kmeans = clustAssing[:, 0].A[:, 0]
    # 未聚类前的数据分布
    plt.subplot(121)
    plt.scatter(X[:, 0], X[:, 1], s=50)
    plt.title("未聚类前的数据分布")
    plt.subplots_adjust(wspace=0.5)
    plt.subplot(122)
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100, alpha=0.5)
    plt.title("用二分K-Means算法原理聚类的效果")
    plt.show()
