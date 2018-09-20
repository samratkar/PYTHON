from sklearn.linear_model import Lasso 
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from adspy_shared_utilities import load_crime_dataset
import numpy as np
from sklearn.datasets import make_regression
from sklearn.preprocessing import MinMaxScaler

'''
DATA SET
'''

X_R1, y_R1 = make_regression(n_samples = 100, n_features=7,
                            n_informative=1, bias = 150.0,
                            noise = 30, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)

#get the scaler
scaler = MinMaxScaler()
#fit the scaler with the data, so that it can measure the min and max of the data.
#fitment is done only on the training set. The same scaler is used to scale test set also!
#THis helps to avoid data leakage from train set to test set.
scaler.fit(X_train)
#transform the data to the new scaled coordinates
X_train_scaled = scaler.transform(X_train)

X_test_scaled = scaler.transform(X_test)

#THe above two steps can be done all together in one go -
X_train_scaled = scaler.fit_transform(X_train)

print ("Ridge regression : alpha trending")
print ("ALPHA           NUMBER OF COEFF         TEST SCORE          TRAIN SCORE")
for this_alpha in [0, 1, 10, 20, 50, 100, 1000]:
    linridge = Ridge (alpha = this_alpha).fit(X_train_scaled, y_train)
    r2_train = linridge.score(X_train_scaled, y_train)
    r2_test = linridge.score(X_test_scaled, y_test)
    print (this_alpha, "            ", np.sum(abs(linridge.coef_)>1.0), "           ", r2_test, "           ", r2_train)
