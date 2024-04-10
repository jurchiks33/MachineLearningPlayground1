import numpy as np
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3, -1.9, -4.3]])

data_standartized = preprocessing.scale(data)
print ("\nMean =", data_standartized.mean(axis=0))
print ("Std deviation =", data_standartized.std(axis=0))
