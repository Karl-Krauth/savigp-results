import pandas as pd
import numpy as np
top = "sarcos_05"
DIR = top + "/predictions.csv"
data_test = pd.read_csv(DIR)
data_train = pd.read_csv(top + "/train.csv")
cols = data_test.columns
dim = 0
for element in cols:
    if element.startswith('true_Y'):
        dim += 1

Ypred = np.array([data_test['predicted_Y_%d' % (d)] for d in range(dim)])
Ytrue = np.array([data_test['true_Y_%d' % (d)] for d in range(dim)])
Yvar = np.array([data_test['predicted_variance_%d' % (d)] for d in range(dim)])

tot = 0.0
for i in range(Ytrue.shape[0]):
    Y_mean = data_train['Y_' + str(i)].mean()
    tot += (((Ypred[i] - Ytrue[i])**2).mean() / ((Y_mean - Ytrue[i]) ** 2).mean())

tot /= Ytrue.shape[0]
print(tot)
