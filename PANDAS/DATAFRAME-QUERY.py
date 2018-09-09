'''
BOOLEAN MASK - AN ARRAY. Multiple conditions can be connected to give a complex query.
'''
import os
import pandas as pd

os.chdir ("/home/samrat/Documents/Git/PYTHON/PANDAS")
#Changing the index to column0 AND skipping the 1st row.
df = pd.read_csv('DATA-FILES/olympics.csv', index_col=0, skiprows=1)
#changing the names of the columns
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns = {col:'Gold'+col[4:]}, inplace = True)
    if col[:2] == '02':
        df.rename(columns = {col:'Silver'+col[4:]}, inplace = True)
    if col[:2] == '03':
        df.rename(columns = {col:'Bronze'+col[4:]}, inplace = True)
    if col[:2] == '№':
        df.rename(columns = {col:'#'+col[4:]}, inplace = True)
df.head()
df['Gold'] > 0
only_gold = df.where(df['Gold']>0)
only_gold = df[df['Gold'] > 0]
only_gold.head()
only_gold = only_gold.dropna()
only_gold.head()
df[(df['Gold.1']>0) & (df['Gold'] == 0)]
