import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
df = pd.read_csv('DATA-FILES/market_fact.csv')
df.head()
#simple density plot or histogram.
sns.distplot (df['Shipping_Cost'])
sns.distplot (df['Sales'])
sns.distplot (df['Profit'])
plt.hist(df['Shipping_Cost'])
sns.FacetGrid(df['Shipping_Cost'])
sns.distplot(df['Sales'], bins = 50)
sns.relplot(df['Sales'], df['Profit'])
