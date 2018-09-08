'''
DATA FRAME INDEXING AND LOADING
'''
import os
import pandas as pd

os.chdir ("/home/samrat/Documents/Git/PYTHON/PANDAS")
df = pd.read_csv('DATA-FILES/olympics.csv')
df.head()
#Changing the index to column0 AND skipping the 1st row.
df = pd.read_csv('DATA-FILES/olympics.csv', index_col=0, skiprows=1)
df.head()
#This is not a list data type. Rather it is 'index' data type from pandas, which behaves as a list of strings.
col_list = df.columns
col_list
type(col_list)
#col_list is a list of strings. So, each element will be a string. And then you can slice strings character wise providin the slicing operators.
a = col_list[0]
a
a[:1]
a[:2]
a[:3]
col = col_list[1]
col
col[:1]
col[:2]
col[:3]
col[:4]
#even u went past the end. no probs.
col[:5]
col[4:]
#in the rename function, inside the dictionary known as column, provide the index as the name of the value of the column you want to replace, and the value to the index:value pair should be the new value.
#df.rename(columns = {'old_value':'new_value'}, inplace=True)
df.rename(columns = {col:'Gold'+col[4:]}, inplace = True)
col
new_col = df.columns[1]
new_col
df.head
#changing the names of the columns
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns = {})
