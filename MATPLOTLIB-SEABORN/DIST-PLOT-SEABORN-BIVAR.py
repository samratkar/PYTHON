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



sns.pairplot(df)
