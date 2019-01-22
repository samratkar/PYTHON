#NOTE 1 - dropna deletes the entire row or column where there is even one NA!!! Na can be nan or NaT
import pandas as pd
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                    pd.NaT]})

df


#Drop the rows where at least one element is missing.
df.dropna()
     name        toy       born
1  Batman  Batmobile 1940-04-25
Drop the columns where at least one element is missing.

>>> df.dropna(axis='columns')
       name
0    Alfred
1    Batman
2  Catwoman
Drop the rows where all elements are missing.

>>> df.dropna(how='all')
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
Keep only the rows with at least 2 non-NA values.

>>> df.dropna(thresh=2)
       name        toy       born
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
Define in which columns to look for missing values.

>>> df.dropna(subset=['name', 'born'])
       name        toy       born
1    Batman  Batmobile 1940-04-25
Keep the DataFrame with valid entries in the same variable.

>>> df.dropna(inplace=True)
>>> df
     name        toy       born
1  Batman  Batmobile 1940-04-25

import pandas as pd
marks = pd.read_csv('https://query.data.world/s/HqjNNadqEnwSq1qnoV_JqyRJkc7o6O')
marks.head()
marks.shape

marks.shape[0]
marks.dropna(thresh = 5)
marks
marks.isnull().sum()
marks.isnull().sum(axis=0)
print (marks.isnull().sum(axis=1))
marks.Final
#print(#Type your code here to get sum of missing values in each column)
