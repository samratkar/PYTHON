# loading libraries and reading the data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set seaborn theme if you prefer
sns.set(style="white")

# read data
market_df = pd.read_csv("DATA-FILES/global_sales_data/market_fact.csv")
customer_df = pd.read_csv("DATA-FILES/global_sales_data/cust_dimen.csv")
product_df = pd.read_csv("DATA-FILES/global_sales_data/prod_dimen.csv")
shipping_df = pd.read_csv("DATA-FILES/global_sales_data/shipping_dimen.csv")
orders_df = pd.read_csv("DATA-FILES/global_sales_data/orders_dimen.csv")
