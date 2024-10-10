import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class per:
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, x, y):
        self.w = np.zeros(1 + x.shape[1])
        self.errors = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(x, y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w[0] += update
                errors += int(update != 0.0)
            self.errors.append(errors)
        return self

    def net_input(self, x):
        return np.dot(x, self.w[1:]) + self.w[0]

    def predict(self, x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)


df=pd.read_csv('iris.data')
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
x = df.iloc[0:100, [0, 2]].values

if __name__=='__main__':
    ppn = per(eta=0.1, n_iter=10)
    ppn.fit(x, y)
    # 显示错误分类数
    plt.figure()
    plt.plot(range(1, len(ppn.errors) + 1), ppn.errors, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassfications')
    plt.show()