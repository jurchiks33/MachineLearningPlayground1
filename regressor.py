import sys
import numpy as np

filename = sys.argv[1]
x = []
y = []
with open(filename, 'r') as f:
    for line in f.realines():
        xt, yt = [float(i) for i in line.split(',')]
        x.append(xt)
        y.append(yt)

num_training = int(0.8 * len(x))
num_test = len(x) - num_training

#Training data
x_test = np.array(x[num_training:]).reshape((num_test, 1))
y_test = np.array(y[num_training:])

