from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from adspy_shared_utilities import load_crime_dataset
import numpy as np
from sklearn.datasets import make_regression

'''
DATA SET
'''

X_R1, y_R1 = make_regression(n_samples = 100, n_features=7,
                            n_informative=1, bias = 150.0,
                            noise = 30, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)

'''
RIDGE REGRESSION
'''
#(X_crime, y_crime) = load_crime_dataset()

#X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime,              random_state = 0)
linridge = Ridge(alpha=20.0).fit(X_train, y_train)
#print ('Crime Dataset')
print ('ridge regression linear model intercept:', linridge.intercept_)
print ('ridge regression linear model coefficients:', linridge.coef_)
print ('ridge regression linear model train score:', linridge.score(X_train, y_train))
print ('ridge regression linear model test score:', linridge.score(X_test, y_test))
print ('number of non zero features:', np.sum(linridge.coef_ != 0))
