import os
path="/home/samrat/Documents/Git/PYTHON/PANDAS"
os.chdir(path)
import pandas as pd
df = pd.read_csv("DATA-FILES/olympics.csv")
df.head()
df.tail()
df.info()
df.describe()
df.columns
df.shape
df.values

