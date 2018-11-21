'''NOTE: WES MCKINNEY - PYTHON FOR DATA ANALYSIS
1. A DataFrame represents a data structure containing an "ORDERED" collection of "COLUMNS", each of which can be a different value type (numeric,string, boolean, etc.)
2. A DataFrame is a Dictionary of Series, where each series is a column.
3. The values of each column is arranged in ascending order
4. Under the hood, the data is stored as one or more two-dimensional blocks rather than a list, dict, or some other collection of one-dimensional arrays.
5. While DataFrame stores the data internally in a two-dimensional for-mat, you can easily represent much higher-dimensional data in a tabular format using hierarchical indexing.

'''
#NOTE - EXAMPLE 1 - DATA FRAMES ARE ORDERED COLLECTION OF COLUMNS !!
import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
      'year' : [2000, 2001, 2002, 2001, 2002],
      'pop'  : [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
df
# NOTE: - conditional indexing!
df[[False, False, True, True, True]]
df[pd.Series([False, False, True, True, True])]
s1 = df['pop'] >2
df[s1]
#NOTE - EXAMPLE 2 - you can change the sequence of columns -
df = pd.DataFrame(data, columns = ['year', 'pop', 'state'])
df
#NOTE - EXAMPLE 3 - you can add new columns simply by appending new ones. If you dont append, the data will be purged
df = pd.DataFrame(data, columns = ['capital', 'minister', 'lit rate'])
df
df = pd.DataFrame(data, columns = ['state', 'year', 'pop', 'capital', 'minister', 'lit rate'])
df
#NOTE - EXAMPLE 4 - INDEXING - you can index the entire column directly in square braces as dataframes are ordered list of columns. Each column is a series that is printed entirely.
df ['state']
type(df['state'])

#NOTE - EXAMPLE 5 - The rows are known as indices. You can specific the rows by providing the index names too!
df = pd.DataFrame(data, index = ['zero', 'one', 'two', 'three', 'four'])
df
#NOTE - EXAMPLE 6 - For nested dictionaries outer index belong to the column names and inner indices are the row indices. Obviously! Since dataframes are collection of columns!
pop = pd.DataFrame({'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}})
pop



# you can change the row idenx of the dataframe
df = pd.DataFrame(data, index = ['Case1'])
'''
1. A dataframe is a table that contains a list of objects of same type!
2. Every row corresponds to one object which has a numberical index. So the entire table is an agregation of multiple objects of the same type.
3. Every column is one attribute to the object.
4. All the data type of each column has to be same. Type is associated with each column.
5. While creating you enter a dictionary of elements to DataFrame. Note that for series, numpy arrays it was enough to supply a list or a tuple of elements.
'''

import pandas as pd
s1 = pd.Series({'First-Name':'Samrat', 'Age': 39, 'Profession':'Professor CS'})
s2 = pd.Series({'First-Name':'Arshia', 'Age': 10, 'Profession':'Professor Physics Harvard'})
s3 = pd.Series({'First-Name':'Raghu', 'Age': 50, 'Profession':'Butler'})
s1
s2
s3
#takes up column names
df = pd.DataFrame({'Class1': s1, 'Class2': s2, 'Class3':s3})
df
df = pd.DataFrame([s1,s2,s3]), index = ['Class1','Class2','Class3'])
df
print (df.loc['Class1'])
print (df.iloc[0])
print (df)
#printing a column. By default the indexing in data frames are wrt columns.
df['Class1']
#printing a row. integer values are used to to mention the row.
df.iloc[0]
#EXERCISE 1
#For the purchase records from the pet store, how would you get a list of all items which had been purchased (regardless of where they might have been purchased, or by whom)?

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
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df
df = pd.DataFrame([purchase_1, purchase_2, purchase_3])
df
print(df['Item Purchased'])
print (df.iloc(1))

#SPLITTING
#Using the list way of splitting you can split only the rows. To be able to split the columns, you will have to add the second argument as given below -
df1 = df.iloc[:,:72] #all columns till 71st column
df2 = df.iloc[:,72:] #columns 72 and beyond.

#NESTED DICTS :
import pandas as pd
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
frame3
pdata = {'Ohio': frame3['Ohio'][:-1],'Nevada': frame3['Nevada'][:2]}
pd.DataFrame(pdata)
Out[63]:
Nevada Ohio
2000
NaN
1.5
2001
2.4
1.7

# NOTE - EVEN NUMBERED ROWS OF A DataFrame
import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
index1 = [i for i in df.index if (i % 2 == 0)]#Type your code here for indexing the dataframe
df_2 = df.iloc[index1[1:]]
print(df_2.head(20))

# NOTE - better solution of the above problem  -
df_2 = df[2: :2]
