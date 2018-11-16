import pandas as pd
market_df = pd.read_csv("DATA-FILES/global_sales_data/market_fact.csv")
customer_df = pd.read_csv("DATA-FILES/global_sales_data/cust_dimen.csv")
product_df = pd.read_csv("DATA-FILES/global_sales_data/prod_dimen.csv")
shipping_df = pd.read_csv("DATA-FILES/global_sales_data/shipping_dimen.csv")
orders_df = pd.read_csv("DATA-FILES/global_sales_data/orders_dimen.csv")
df_1 = pd.merge(market_df, customer_df, how = 'inner', on = 'Cust_id')
df_2 = pd.merge(df_1,product_df,how='inner',on='Prod_id')
df_3 = pd.merge(df_2, shipping_df, how='inner', on='Ship_id')
master_df = pd.merge (df_3,orders_df,how='inner',on='Ord_id')

master_df.head()

df_by_segment = master_df.groupby('Customer_Segment')
df_by_segment
df_by_segment['Profit']
df_by_segment['Profit'].sum()
df_by_segment['Profit'].describe()
'''
Dataframe grouping
Description
Group the data 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind'.
'''
import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
#Type your groupby command here
df_1 = df.groupby(['month','day'])[['rain', 'wind']].mean()#Type your code to find the mean of columns 'rain' and 'wind'
print(df_1.head(20))

'''
Dataframe Pivot Table
Description
Group the data 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind' using the pivot table command.
'''

import numpy as np
import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_1 = df.pivot_table(values = ['rain','wind'], index = ['month','day'], aggfunc = 'mean') #Type your code here.
print(df_1.head(20))
