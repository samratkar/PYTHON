import pandas as pd
import sys as sys
market_df = pd.read_csv("DATA-FILES/global_sales_data/market_fact.csv")
market_df.head()
customer_df = pd.read_csv("DATA-FILES/global_sales_data/cust_dimen.csv")
customer_df.head()
product_df = pd.read_csv("DATA-FILES/global_sales_data/prod_dimen.csv")
shipping_df = pd.read_csv("DATA-FILES/global_sales_data/shipping_dimen.csv")
orders_df = pd.read_csv("DATA-FILES/global_sales_data/orders_dimen.csv")
print (market_df.head())
print (customer_df.head())
customer_df.info()
market_df.info()
market_df.head()
df_1 = pd.merge(market_df, customer_df, how = 'inner', on = 'Cust_id')
#gives error because join by default uses the index of the right table. Here Cust_id is string but the index is integer.
market_df.join(customer_df, on = "Cust_id")
df_1.head()
#NOTE - Dataframe is a collection of series, where each series is one column. So, while creating the dataframe by hand just keep that in mind to create serieses such that they correspond to each column.
import pandas as pd
df1 = pd.DataFrame({'Name'  : ['Ram', 'Shyam', 'Jadhu', 'Madhu'],
                    'Age'   : [20,21,22,23],
                    'Gener' : ['M', 'M', 'M', 'F']})
df2 = pd.DataFrame({'Name'  : ['A', 'B', 'C', 'D'],
                    'Age'   : [10,11,12,13],
                    'Gener' : ['M', 'F', 'M', 'F']})
df3 = pd.DataFrame({'Name'  : ['P', 'Q', 'R', 'S'],
                    'Age'   : [30,31,32,33],
                    'Gener' : ['M', 'M', 'M', 'F']})

pd.concat([df1,df2,df3])
df2+df3

#This is  a method only on the dataframe instance and not on pandas class directly. Also it concats row wise.
df1.append(df2)
pd.concat([df1,df2,df3], axis = 1)

'''
You can also perform various mathematical operations between two or more dataframes. Below is a list of functions that you can use for the same:

add(): +
sub(): -
mul(): *
div(): /
floordiv(): //
mod(): %
pow(): **
'''
'''
Description
Given three data frames containing the number of gold, silver, and bronze Olympic medals won by some countries, determine the total number of medals won by each country.
Note: All the three data frames don’t have all the same countries. So, ensure you use the ‘fill_value’ argument (set it to zero), to avoid getting NaN values. Also, ensure you sort the final dataframe, according to the total medal count in descending order.
'''
import numpy as np
import pandas as pd
#NOTE - GROUPBY
# Defining the three dataframes indicating the gold, silver, and bronze medal counts
# of different countries
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15.0, 13.0, 9.0]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )
# NOTE - METHOD 1

# Set the index of the dataframes to 'Country' so that you can get the countrywise
# medal count
gold.set_index('Country', inplace = True)
silver.set_index('Country', inplace = True)
bronze.set_index('Country', inplace = True)

# Add the three dataframes and set the fill_value argument to zero to avoid getting
# NaN values
# The trick is that the add() method is not adding the country name as they are made into index. This is a smart way to avoid a column gettin summed up. Just make it an index. Otherwise, due to the add() method the names would have got repeated for each row.
total = gold.add(silver, fill_value = 0).add(bronze, fill_value = 0)

# Sort the resultant dataframe in a descending order
total = total.sort_values(by = 'Medals', ascending = False)

# Print the sorted dataframe
print(total)

# NOTE - METHOD 2

df_merged = pd.concat([gold,silver,bronze])
df_merged.sort_values('Medals', ascending = False, inplace = True)
group = df_merged.groupby('Country', sort = True)
grouped = group.agg(np.sum)
grouped.sort_values('Medals', ascending = False, inplace = True)
print(grouped)

##NOTE - Types of joins
inner = intersection of indices
outer = union of indices
left = all rows of the left will be part of the final merged table
right = all from right table
