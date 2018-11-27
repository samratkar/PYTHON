import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('DATA-FILES/market_fact.csv')
#Scatter plot using matplotlib
plt.scatter(df['Sales'], df['Profit'])
plt.show()
#Scatter using seaborn
sns.jointplot('Sales', 'Profit', df)
sns.jointplot(df['Sales'], df['Profit'])
plt.show()

#zooming in
df1 = df[(df['Sales'] < 20000) & (df['Profit'] < 10000)]
sns.jointplot(df1['Sales'], df1['Profit'])
df = pd.read_csv('DATA-FILES/market_fact.csv')
df1 = df[(df['Sales'] < 100) & (df['Profit'] > -100) & (df['Sales'] < 200)]
sns.jointplot(df['Sales'], df['Profit'], kind = 'hex')
plt.show()
#HEAT MAP


df = pd.read_csv('DATA-FILES/market_fact.csv')
sns.pairplot(df)
plt.show()
