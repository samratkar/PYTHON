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
