# Adding up the missing values (column-wise)
telecom.isnull().sum()
#Find the percentage of the total null values.
# Checking the percentage of missing values
round(100*(telecom.isnull().sum()/len(telecom.index)), 2)

#If the percentage is less, just remove them as follows -
# Removing NaN TotalCharges rows
telecom = telecom[~np.isnan(telecom['TotalCharges'])]
