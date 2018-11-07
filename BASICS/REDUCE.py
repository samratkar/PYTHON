from functools import reduce
# -*- coding: utf-8 -*-
#
#Description
#Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
#If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

from functools import reduce

#write your code here.
print(reduce (lambda x,y : x+ " " + y, input_list))

# find the largest number from a list
print(reduce (lambda x,y: x if x>y else y, input_list))

#QUESTION - FIND THE FACTORIAL OF A LIST OF NUMBERS ENTERED. 

# Read the input as an integer
n = int(input())

# Import the reduce() function
from functools import reduce

# Write your code here
if n == 0 :
    print (1)
    exit()
    
my_list = [i for i in range(1,n+1)]
print (reduce ((lambda x,y: x*y), my_list))
