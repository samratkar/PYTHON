#1. ARRAY CREATION
import numpy as np
mylist=[1,2,3,4]
print (mylist)
x = np.array(mylist)
print (x)
y = np.array([4,5,6])
print (y)
#2 dimensional matrix in numpy
z = np.array([[7,8,9],[10,11,12]])
print(z)
#2 dimensional matrix in normal list
mylist2 = [[1,2], [4,5], [7,8]]
print (mylist2)
m = np.array(mylist2)
print(m)

#2. SHAPE AND SIZING
print(m.shape)
#printing a series - airthmetic progress
import numpy as np
a = np.arange (0,30,2)
print (a)
b = np.linspace(0,4,20)
print (b)
c = a.reshape(3,5)
print (c)
print (a)
#resize returns none and changes the shape of the original matrix.
d = a.resize(3,5)
print ("d=", d)
print (a)

#3. STANDARD MATRICES
import numpy as np
print (np.ones((5,6)))
print (np.zeros((5,6)))
print (np.eye(5))
#print (np.diag())

#4. repeatst6g
import numpy as np
print (np.repeat([1,2,3],3))
print(np.array([1,2,3]*3))

#matrix arithmetic
import numpy as np
x = np.array([[7,8,9],[10,11,12]])
y = np.array([[5,6,7],[8,9,10]])
print(x.sum())
print(x.max())
print(x.min())
print(x.mean())
print(x.std())
print(x.argmax())
print(x.argmin())

#SLICING AND INDEXING
import numpy as np
a = np.arange(30)
print (a[5:])
print (a[-5:])
print (a[5:29])
print (a[5::2])
print (a[-5::-2])
print (a[-5::2])

import numpy as np
b = np.arange(30)
b.resize(6,6)
print (b)
print (b[2:3])
print (b[2:4])
print (b[2:6])
print (b[1::3])
print (b[2,2:])
print (b[0::2, 0::2])
print (b[b>15])
b[b>15]= 99
print (b)
#numpy array does not create a copy unless .copy() method is called. even if you assign the value to a new variable, the previous matrix gets changed.

#CREATING A RANDOM MATRIX -
import numpy as np
test = np.random.randint(0,4,(4,3))
print(test)

#ENUMERATION
for row_num, row_val in enumerate (test):
    print ( 'row:', row_num, 'is', row_val)
