import numpy as np
array_1d = np.arange(1,20,2)
print (array_1d)

#accessing by providing a list of indices!
print (array_1d[[2,3,4]])

'''
you can use all the slicing mechanisms to access subset of the array as ou do in the list
ACCESSIN MULTIDIMENSIONAL ARRAY
IN NORMAL PYTHON LIST, YOU USE SQUARE BRACES TO ACCESS ONE ELEMENT FROM THE ARRAY. IN NUMPY IT IS ABOUT ACCESSING AS ELEMENTS OF A MATRIX. BUT THE INDICES NEED TO BE PLACED WITHIN SQUARE BRACES. FOR EACH ELEMENTS WITHIN THE COMMAS, THE COLON SLICING FOLLOWS THE SAME CONVENTION
'''

#2D Array
#Description
#From a 2D array extract all the rows of the 2 column.
#Hint: 2 column will have index value as 1.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
import numpy as np
array_2d =np.array(input_list)

print(array_2d[:,1])
