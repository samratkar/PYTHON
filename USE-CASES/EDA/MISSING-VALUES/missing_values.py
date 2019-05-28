# Adding up the missing values (column-wise)
telecom.isnull().sum()
#Find the percentage of the total null values.
# Checking the percentage of missing values
round(100*(telecom.isnull().sum()/len(telecom.index)), 2)

#IF MISSING VALUE PERCENTAGE IS NEAR 17%
#If the percentage of not null is less, just remove the rows with null values as follows
# Removing NaN TotalCharges rows. Imputing mean or median into null values if most of the entries are null is not the right thing to do, as it will bias the data. even if the number of rows with null values are 17% it is better to delete the rows
telecom = telecom[~np.isnan(telecom['TotalCharges'])]

#IF MISSING VALUE PERCENTAGE IS LESS, SAY 6%
country_codes = master['country_code'].astype('category')
# displaying frequencies of each category. value_counts does not work with raw string data type. So we converted it to category.
country_codes.value_counts()

Note that np.isnan does not work with arrays of type 'object', it only works with native numpy type (float). Thus, you can use pd.isnull() instead.
