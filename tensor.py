import tensorflow as tf
import numpy as np

x=[[1]]
m=tf.matmul(x,x)
print(m)
x= tf.constant([[1,9],[3,6]])
print(x)
x=tf.add(x,1)
