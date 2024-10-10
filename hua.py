import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
iris=datasets.load_iris()
x=iris.data[:,[2,3]]
y=iris.target