import numpy as np 
import pandas as pd
#import tensorflow as tf
import matplotlib.pyplot as plt
pata = np.arange(9)
print(pata)

from numpy import random
data = (np.arange(9))
print(random.choice(data,3))

data1 = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
print(type(data))
print("第一組的維度:",data1.ndim)
data2 = np.array([[9, 2, 3], [4, 10, 6], [7, 8, 5]])
print(type(data))
print("第二組的維度:",data2.ndim)
data3 = np.array([[[9, 2, 3], [4, 10, 6]], [[7, 8, 1], [5, 0, 11]]])
print(type(data))
print("第三組的維度:",data2.ndim)

