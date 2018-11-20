import numpy as np
import pandas as pd
df = pd.read_csv("DATA-FILES/melbourne.csv")
df.head()
df.describe()

#NOTE 1 - DETECTING MISSING VALUES.
df.shape
    #This helps you to figure out the extent of null values in the dataframe.
df.info()
    #makes those values as TRUE that are missing.
df.isnull()
    #column wise sum of nulls
df.isnull().sum() > 5
    #columnwise sum
df.isnull().sum()
    #if a column as any true, it is marked as true.
df.isnull().any()
df.isnull().any(axis = 1)
df.isnull().all(axis = 1)
    #Finding the percentage of missing values
round(100*df.isnull().sum()/len(df.index),2)
    #Checking for null values in rows -
df.isnull().sum(axis=1) > 5
    #Count of such rows
len((df.isnull().sum(axis=1) > 5).index)
#FIXING THE MISSING VALUES
    #dropping columns that are not required.
df = df.drop('BuildingArea', axis = 1)

# NOTE - Removing Missing Values From the Rows
# Description
# Remove the missing values from the rows having greater than 5 missing values and then print the percentage of missing values in each column.
import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df = df[df.isnull().sum(axis=1) <= 5]

print(round(100*(df.isnull().sum()/len(df.index)), 2))#Round off to 2 decimal places.

##NOTE - Mean Imputation
#Description
#Impute the mean value at all the missing values of the column 'Product_Base_Margin' and then print the percentage of missing values in each column.

import numpy as np
import pandas as pd
df = pd.read_csv('https://query.data.world/s/Hfu_PsEuD1Z_yJHmGaxWTxvkz7W_b0')
df.loc[np.isnan(df['Product_Base_Margin']), ['Product_Base_Margin']] = df['Product_Base_Margin'].mean()
print(round(100*(df.isnull().sum()/len(df.index)), 2))
