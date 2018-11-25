import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("DATA-FILES/market_fact.csv")
df.head()

#NOTE - BOXPLOT
plt.boxplot(df['Order_Quantity'])
plt.boxplot(df['Sales'])
df['Sales'].describe()

#NOTE - HISTOGRAM
plt.hist(df['Order_Quantity'])
plt.hist(df['Sales'])
plt.scatter(df['Sales'], df['Profit'])
