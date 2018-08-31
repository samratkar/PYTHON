import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
import mglearn

import os
path="/home/samrat/Documents/Git/PYTHON/SKLEARN"
os.chdir(path)
import pandas as pd
fruit_table = pd.read_table("DATA-SET/fruit_data_with_colors.txt")
fruit_table.head()
fruit_table

X = fruit_table [['mass', 'width', 'height', 'color_score']]
y = fruit_table['fruit_label']
from sklearn.model_selection import train_test_split
#y_train and y_test are scalar. X_train and X_test are vectors.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
X_train
X_test
#2d scatter_matrix
from matplotlib import cm
cmap = cm.get_cmap('gnuplot')
scatter = pd.scatter_matrix(X_train, c= y_train, marker ='o', s=40, hist_kwds = {'bins':15}, figsize=(12,12),cmap =cmap)

#3d scatter matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(X_train['width'],X_train['height'], X_train['color_score'],c=y_train, marker = 'o', s=100 )
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()
