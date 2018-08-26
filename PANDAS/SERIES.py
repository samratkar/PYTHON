import pandas as pd
import numpy as np 
animals = ['Tiger', 'Bear', 'Moose']
#the data type is written by default
pd.Series(animals)
animals 
numbers = [1,2,3,4]
pd.Series(numbers)
#Not a number - None in python is automatically converted to None for strings and Nan for numbres by pandas.
numbers = [1,2,3,None]
pd.Series(numbers)
animals = ['Tiger', 'Bear', 'Moose', None]
pd.Series(animals)

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








