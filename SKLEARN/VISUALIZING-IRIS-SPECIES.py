import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
#import mglearn

iris_dataset = load_iris()
#the data set is not a pandas frame. So, you will not be able to print head
type(iris_dataset)
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
#1. Print the description of the data set.
print(iris_dataset.DESCR)
#2. Print the keys to undrestand the schema of the data. Note that head() does not work here as it is not a panda data frame
iris_dataset.keys()
#3. Printing the raw data set
print (iris_dataset)
#4. Number of features
print (len (iris_dataset['feature_names']))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# create a scatter matrix from the dataframe, color by y_train
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
hist_kwds={'bins': 20}, s=60, alpha=.8) #, cmap=mglearn.cm3)
plt.show()
