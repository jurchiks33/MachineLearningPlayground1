import sys
import numpy as np

from sklearn import linear_model
import matplotlib.pyplot as plt

filename = sys.argv[1]
x = []
y = []
with open(filename, 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        x.append(xt)
        y.append(yt)

num_training = int(0.8 * len(x))
num_test = len(x) - num_training

#Training data
x_train = np.array(x[:num_training]).reshape((num_training, 1))
y_train = np.array(y[:num_training])

#Test data
x_test = np.array(x[num_training:]).reshape((num_test, 1))
y_test = np.array(y[num_training:])

#Create linear regression object
linear_regressor = linear_model.LinearRegression()

#Train model using the training sets
linear_regressor.fit(x_train, y_train)

y_train_pred = linear_regressor.predict(x_train)
plt.figure()
plt.scatter(x_train, y_train, color='green')
plt.plot(x_train, y_train_pred, color='black', linewidth=4)
plt.title('Training data')
plt.show()

y_test_pred = linear_regressor.predict(x_test)

plt.scatter(x_test, y_test, color='green')
plt.plot(x_test, y_test_pred, color='black', linewidth=4)
plt.title('Test data')
plt.show()

###########################################
#Run data with 'python regressor.py data/data_singlevar.txt'
#First will apear train_pred and after test_pred.
###########################################

