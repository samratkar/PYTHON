import numpy as np
import pandas as pd
df = pd.read_csv("DATA-FILES/melbourne.csv")
df.head()
df.describe()

#DETECTING MISSING VALUES.
df.shape
#This helps you to figure out the extent of null values in the dataframe.
df.info()
#makes those values as TRUE that are missing.
df.isnull()
#columnwise sum
df.isnull().sum()
#if a column as any true, it is marked as true.
df.isnull().any()
df.isnull().any(axis = 1)
df.isnull().all(axis = 1)

#FIXING THE MISSING VALUES
