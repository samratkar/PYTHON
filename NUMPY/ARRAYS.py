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
print (np.diag())

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

a.resize(6,6)
print (a)


