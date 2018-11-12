'''
NOTES -
1. If dictionary is passed into the series as input, then the mapping between the values and the indices are maintained. This can be seen in the example in line# 26. This tight linkage between the index and the values are not maintained if the input to the series is a list as shown in the example above it. So, for the new index a new  entry is added, and the existing mapptings are not even distrubed. The entry for which indices does not occur in the new index list are omitted outright. This is a way to filter out data!!
But if the input is just a list, then the mappings are disturbed and indices are updated in order of the entry of the new indices. 

2. Since pandas are built on the top of the numpy array, all the broadcasting of operations (vectorization) is enabled by default with pandas. So, lambda functions and mapping them to the data strcutures are no more required.

'''

import pandas as pd
import numpy as np
animals = ['Tiger', 'Bear', 'Moose']
#the data type is written by default
animals
animals_series = pd.Series(animals)
animals_series
animals_series[[0,2]]
numbers = [1,2,3,4]
pd.Series(numbers)
#Not a number - None in python is automatically converted to None for strings and Nan for numbres by pandas.
numbers = [1,2,3,None]
pd.Series(numbers)
animals = ['Tiger', 'Bear', 'Moose', 'Lion']
pd.Series(animals)
pd.Series(animals, index = ['a','b','c','d'])
pd.Series(animals, index = ['a','x','c','d'])

## NOTE : INDEX REHASHING WITH DICT INPUT
import pandas as pd
sdata = {'a':'Tiger', 'b':'Bear', 'c':'Moose', 'd': 'Lion'}
obj3 = pd.Series(sdata)
obj3
obj4 = pd.Series(sdata, index = ['a', 'x', 'c', 'd'])
obj4
#dictionary into Series
sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo':'Japan', 'Taekwando': 'South Korea'}
s = pd.Series(sports)
s.index
#providing the index separately from data.
s = pd.Series(['Tiger','Bear','Moose'], index = ['India', 'Canada', 'Austrailia'])
s

#quering
s.iloc[0]
s[0]
s.loc['India']
s['India']

sports = {24: 'Bhutan', 25: 'Scotland', 26:'Japan', 27: 'South Korea'}
s = pd.Series(sports)
s
#error as index are not 0
s[0]
s[24]
s.iloc[0]

# working with data
s = pd.Series([100,200,300,400])
#vectorization of sum
s.sum()

s = pd.Series(np.random.randint(0,1000,10))
s.head

# NOTE: apply()
import pandas as pd
series_1 = pd.Series([1,2,3,4])
series_1
series_1*2
series_1**2

# NOTE: QUESTION 1
'''
Create a panda series that contains the first ‘n’ natural numbers and their respective squares. The first ‘n’ numbers should appear in the index position.
Hint: Use manual indexing.
'''
n = int(input())

import numpy as np
import pandas as pd
n = 5
data1 = np.array(range(1,n+1))
series1 = pd.Series(data1**2, index = data1 )
print(series1)
series1 [1]

# NOTE : set_index() sort_index()

df.set_index ('Order_index', inplace = True)
df.sort_index(ascending = False )
df.sort_values(by='Sales')
df.sort_values(by=['Sales','Product_id'])


