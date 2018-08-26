import os
path="/home/samrat/Documents/Git/PYTHON/PANDAS"
os.chdir(path)
import pandas as pd
df = pd.read_csv("DATA-FILES/olympics.csv")
df.head()
