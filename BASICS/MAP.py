print("hi there")
store1 = [10.00, 11.00, 12.00, 2.34]
min(store1)
store2 = [1.11, 9.22, 10.99, 13]
# min will be applied one by one to the elements each taken from the list in the argument. First element of store1 is taken along with the 1st element of store 2 and it goes one. THen second element is taken from each list.
str.lower('N')

min_val = map(min, store1, store2)
print (list(min_val))


# SPLITTING NAMES USING MAP
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    split_name = person.split()
    return split_name[0]+split_name[-1]

list(map(split_title_and_name, people))

#NOTE : square the elements of a list
my_list = [1,2,3,4,5,6]
print (list(map(lambda x:x**2, my_list)))

#NOTE : count all the entries which start with S
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
s_list = list()
count = 0
my_list = list(map(lambda x: 1 if (x[0] == 'S') else 0, input_list))
count = sum(my_list)
print(count)

#Direct mapping - correct.
import pandas as pd
df = pd.DataFrame({'Name': name,'Response': response})

# Define a function to map the categorical variables to appropriate numbers
# Note that series has a .map() method. You can directly map items in a series directly as follows. 
def response_map(x):
    return x.map({'Yes': 1, 'yes': 1, 'No': 0, 'no': 0, 'Maybe': 0.5, 'maybe': 0.5})

# Apply the function to the 'Response' column of the dataframe
df[['Response']] = df[['Response']].apply(response_map)

# Print the final DataFrame
print(df)
