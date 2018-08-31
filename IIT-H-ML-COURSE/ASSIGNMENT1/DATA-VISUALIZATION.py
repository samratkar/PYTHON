import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
path="/home/samrat/Documents/Git/PYTHON/IIT-H-ML-COURSE"
os.chdir(path)
import pandas as pd
df = pd.read_csv ("ASSIGNMENT1/DATA/wine-dataset.csv")
X = df.loc[:, df.columns != 'quality']
y = df.loc[:, df.columns == 'quality']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#2d scatter_matrix
#from matplotlib import cm
#cmap = cm.get_cmap('gnuplot')
#scatter = pd.plotting.scatter_matrix(X_train, figsize=(11,11))
#plt.show()

#create a classifier object -
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
