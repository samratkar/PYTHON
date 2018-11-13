'''
1. As Prof Raghavan said, each row of a data frame is an object of the same type. The type of each of the objects is determined by the type of the columns. The schema of the columns is determined by the constituent series'.
'''
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 2', 'Store 3'])
#NOTE: ACCESSING USING THE ROW NAME GIVES YOU ALWAYS A DATA FRAME
df
df['Store 1' : 'Store 3']
df['Store 1':]
ss = df.loc['Store 1']
print (ss)
#NOTE: data type is series. a table is not created as a data frame
print (type(ss))
#NOTE : Now since a list of attributes are provided the data type of output is a dataframe
df.loc[['Store 1', 'Store 2']]
#NOTE : ss is a data frame now!
ss = df.loc[['Store 1']]
print (ss)
print (type(ss))
ss1 = df['Name']
print (ss1)
type(ss1)
df.loc[:]
df[:]
df.iloc[0]
df.loc['Store 1', 'Name']
df.loc['Store 1', 'Cost']
df.iloc[0,0]
df.iloc[0,2]
df1 = pd.DataFrame([purchase_1, purchase_2, purchase_3])
df1
df[::]

#NOTE : Using iloc index the dataframe to print all the rows of the columns at index 3,4,5.
#Hint: Use 3,4,5 not 2,3,4
import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.iloc[:,3:6]#Type your code for indexing using iloc
print(df_2.head(20))

'''
CONDITION BASED INDEXING
'''

import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df.head()
df[df['area'] > 0]
