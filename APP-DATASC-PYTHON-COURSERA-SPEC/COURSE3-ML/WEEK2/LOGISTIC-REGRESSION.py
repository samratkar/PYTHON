from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from adspy_shared_utilities import load_crime_dataset
from adspy_shared_utilities import (plot_class_regions_for_classifier_subplot)
import pandas as pd

fruits = pd.read_table('fruit_data_with_colors.txt')
feature_names_fruits = ['height', 'width', 'mass', 'color_score']
X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']
target_names_fruits = ['apple', 'mandarin', 'orange', 'lemon']

X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']

fig, subaxes = plt.subplots(1,1,figsize = (7,5))
y_fruits_apple = y_fruits_2d == 1
X_train, X_test,  y_train, y_test = (
train_test_split(X_fruits_2d.as_matrix(),
                y_fruits_appple.as_matrix(),
                random_state = 0)    )


from sklearn.datasets import make_regression
