# NOTE: METHOD 1

Replace Values
Let's start with the most basic method, which is just replacing the categories with the desired numbers. This can be achieved with the help of the replace() function in pandas. The idea is that you have the liberty to choose whatever numbers you want to assign to the categories according to the business use case.

You will now create a dictionary which contains mapping numbers for each category in the carrier column:

replace_map = {'carrier': {'AA': 1, 'AS': 2, 'B6': 3, 'DL': 4,
                                  'F9': 5, 'HA': 6, 'OO': 7 , 'UA': 8 , 'US': 9,'VX': 10,'WN': 11}}

Note that defining a mapping via a hard coded dictionary is easy when the number of categories is low, like in this case which is 11. You can achieve the same mapping with the help of dictionary comprehensions as shown below. This will be useful when the categories count is high and you don't want to type out each mapping. You will store the category names in a list called labels and then zip it to a seqeunce of numbers and iterate over it.

labels = cat_df_flights['carrier'].astype('category').cat.categories.tolist()
replace_map_comp = {'carrier' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}

print(replace_map_comp)

{'carrier': {'AA': 1, 'OO': 7, 'DL': 4, 'F9': 5, 'B6': 3, 'US': 9, 'AS': 2, 'WN': 11, 'VX': 10, 'HA': 6, 'UA': 8}}

# NOTE: METHOD 2
# Define a function to map the categorical variables to appropriate numbers
# Note that x passed below is a series. Series has a method map() to do exactly this! And all columns are series.
def response_map(x):
    return x.map({'Yes': 1, 'yes': 1, 'No': 0, 'no': 0, 'Maybe': 0.5, 'maybe': 0.5})

# Apply the function to the 'Response' column of the dataframe
df[['Response']] = df[['Response']].apply(response_map)

# Print the final DataFrame
print(df)
