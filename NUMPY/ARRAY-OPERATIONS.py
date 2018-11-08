# NOTE : 1 - RESHAPE TO ANY SIZE
import numpy as np
array_1 = np.arange (24)
print(array_1)
array_1.reshape(3,-1)
array_1.reshape(8,3)

#NOTE : 2 - transpose
array_1.T

# NOTE : 3 - HORIZONTAL AND VERTICAL STACKING
np.hstack((array_1,array_1))

# Read the input
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]

# Import NumPy
import numpy as np

# Write your code here
array_1 = np.array(list_1)
array_2 = np.array(list_2)
array_4 = np.hstack((array_1, array_2))
array_3 = np.array(list_3)
array_5 = np.vstack((array_4, array_3))
print (array_5)

# NOTE : VECTORIZE
# YOU CAN VECTORIZE ANY OF YOUR FUNCTIONS USING np.vectorize(array)
