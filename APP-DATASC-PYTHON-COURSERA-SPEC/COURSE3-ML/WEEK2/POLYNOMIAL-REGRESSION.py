from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import make_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
'''
DATA SET
'''

X_R1, y_R1 = make_regression(n_samples = 100, n_features=7,
                            n_informative=1, bias = 150.0,
                            noise = 30, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)

poly = PolynomialFeatures(degree=2)
#Transforming normal feature matrix to polynomial matrix.
X_poly_transform_train = poly.fit_transform(X_train)
X_poly_transform_test = poly.fit_transform(X_test)


linreg = LinearRegression().fit(X_poly_transform, y_train)

print('linear model coeff (w): {}'.format(linreg.coef_))
print('linear model intercept (b): {:.3f}'.format(linreg.intercept_))
print('R-squared score (training): {:.3f}'.format(linreg.score(X_poly_transform_train, y_train)))
print('R-squared score (test): {:.3f}'.format(linreg.score(X_poly_transform_test, y_test)))
