import numpy as np
a = np.arange(1,10).reshape(3,3)
b = np.arange(1,13).reshape(3,4)
print (a)
print (b)
np.linalg.det(a)
np.linalg.inv(a)
np.linalg.eig(a)
#matrix multiplication
np.dot(a,b)

#NOTE 1 -
Example 1-
The frequency table of words in four sample emails is shown below. The angle between emails 1 and 2 is (the first two rows):

money	hurry	meeting	powerpoint
2   	1	     0	      0
0	    0	     1	      1
1	    1	     0	      0
1	    1	     1	      0

import numpy as np
e1 = np.array([2,1,0,0])
e2 = np.array([0,0,1,1])
e3 = np.array([1,1,1,0])
dot_prod = np.dot(e1,e2)

#NOTE 2 -
Angle Between Emails
The frequency table of words in four sample emails is shown below. You want to know whether email number 4 (the last row) is more similar to email 1 or email 3. Choose all the correct options.

money	hurry	meeting	powerpoint
2	1	0	0
0	0	1	1
1	1	0	0
1	1	1	0

import numpy as np
e1 = np.array([2,1,0,0])
e2 = np.array([0,0,1,1])
e3 = np.array([1,1,0,0])
e4 = np.array([1,1,1,0])
dot_prod = np.dot(e1,e2)
dot_prod_1_4 = np.dot(e1,e4)
dot_prod_3_4 = np.dot(e3,e4)
ang_1_4 = np.arccos(dot_prod_1_4/(np.sqrt(5)*np.sqrt(3)))*(180/np.pi)
ang_3_4 = np.arccos(dot_prod_3_4/(np.sqrt(2)*np.sqrt(3)))*(180/np.pi)

import numpy as np

A = np.array([[1, 2],
             [2, 0]])
B = np.array([[0, 1],
             [-1, 2]])

# matrix addition
print(A+B)

# matrix product
print(np.dot(A, B))


import numpy as np
A = np.array([[1, 3],
             [2, 0]])
# transpose
print(A.T)

#NOTE - LINEAR TRANSFORMATION -
1. COUNTER CLOCKWISE 90 DEGREE
2. SHEAR
3. CLOCKWISE 90 DEGREE

ninety_degree_counter_clockwise = np.array([[0, -1],
                                            [1, 0]])
ninety_degree_clockwise = np.array([[0, 1],
                                    [-1, 0]])
shear = np.array([[1,1],
                  [0,1]])
temp = np.dot(shear,ninety_degree_counter_clockwise)
transformed = np.dot(ninety_degree_clockwise,temp)
print (transformed)

# NOTE: system of three equations
import numpy as np
A = np.array([[2, 6, -1],
              [1, 2, -2],
              [-5,0,  2]])
b = np.array([0, 1, 8])

# compute the inverse
A_inv = np.linalg.inv(A)

# solution: A_inv * b
x = np.dot(A_inv, b)
print(x) # returns [ 0.  0. -1.]
