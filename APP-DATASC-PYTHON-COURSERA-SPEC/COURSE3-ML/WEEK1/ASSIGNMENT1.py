#Assignment 1 - Introduction to Machine Learning
#For this assignment, you will be using the Breast Cancer Wisconsin (Diagnostic) Database to create a classifier that can help diagnose patients. First, read through the description of the dataset (below).

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
#The object returned by load_breast_cancer() is a scikit-learn Bunch object, which is similar to a dictionary.​
cancer = load_breast_cancer()
print(cancer.DESCR) # Print the data set description
cancer.keys()
