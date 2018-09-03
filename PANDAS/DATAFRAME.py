import pandas as pd
s1 = pd.Series({'First-Name':'Samrat', 'Age': 39, 'Profession':'Professor CS'})
s2 = pd.Series({'First-Name':'Mohan', 'Age': 40, 'Profession':'IT Professional'})
s3 = pd.Series({'First-Name':'Raghu', 'Age': 50, 'Profession':'Butler'})
s1
s2
s3
#takes up column names
df = pd.DataFrame({'Class1': s1, 'Class2': s2, 'Class3':s3})
print (df)
df = pd.DataFrame([s1,s2,s3], index = ['Class1','Class2','Class3'])
print (df)
print (df.loc['Class1'])
print (df.iloc[0])
print (df)

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
print (df)
print(df['Item Purchased'])

#SPLITTING
#Using the list way of splitting you can split only the rows. To be able to split the columns, you will have to add the second argument as given below -
df1 = df.iloc[:,:72] #all columns till 71st column
df2 = df.iloc[:,72:] #columns 72 and beyond.
