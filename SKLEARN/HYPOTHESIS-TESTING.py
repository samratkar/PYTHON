1-sample t-test: testing the value of a population mean
To test, if the population mean of data is likely to be equal to a given value

scipy.stats.ttest_1samp()

stats.ttest_1samp(data['column'], x)
#where x is the mean value you want to test

2-sample t-test: testing for difference across populations
scipy.stats.ttest_ind()

stats.ttest_ind(column_1,column_2)



Paired tests: repeated measurements on the same individuals
stats.ttest_rel()

stats.ttest_rel(column_1,column_2)
