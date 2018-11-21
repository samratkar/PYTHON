#QUESTION 1
#Description
#Given m and n, swap the mth and nth rows of the 2-D NumPy array given below.

#a = [[4 3 1]
#        [5 7 0]
#         [9 9 3]
#         [8 2 4]]

import numpy as np
# Given array
a = np.array([[4, 3, 1], [5, 7, 0], [9, 9, 3], [8, 2, 4]])
temp=a[0]
a[3]
# Read the values of m and n
m = int(input ('enter m'))
n = int (input ('enter n'))

# Write your code for swapping here
## NOTE - NORMAL ASSIGNMENT IS PASS BY REFERENCE. SO YOU NEED TO USE COPY() EXPLICITYLY
temp = a[m].copy()
a[m] = a [n].copy()
a[n] = temp
# Print the array after swapping
print(a)

#QUESTION 2
#Create border array
#Description
#Given a single integer n, create an (n x n) 2D array with 1 on the border and 0 on the inside.
#Note: Make sure the array is of type int.
# Read the variable from STDIN
n = int(input())

import numpy as np
a = np.ones((n,n), dtype = np.int)
a[1:-1, 1:-1] = 0
print (a)
