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
sns.distplot (df['Shipping_Cost'][:200], rug=True)
sns.distplot (df['Shipping_Cost'][:200], hist=False)

#Sets the bins for the histogram. If you make hist as false, then you will not be able to see the difference in setting different bins.
sns.distplot (df['Shipping_Cost'][:200], bins = 50)

plt.hist(df['Shipping_Cost'])

sns.boxplot(df['Order_Quantity'])
sns.boxplot(y=df['Order_Quantity'])
sns.distplot(df['Sales'][:1000], rug = True)

# subplots

# subplot 1
plt.subplot(2, 2, 1)
plt.title('Sales')
sns.distplot(df['Sales'])

# subplot 2
plt.subplot(2, 2, 2)
plt.title('Profit')
sns.distplot(df['Profit'])

# subplot 3
plt.subplot(2, 2, 3)
# plt.title('Order Quantity')
sns.distplot(df['Order_Quantity'])

# subplot 4
plt.subplot(2, 2, 4)
# plt.title('Shipping Cost')
sns.distplot(df['Shipping_Cost'])

plt.show()
