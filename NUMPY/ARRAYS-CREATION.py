'''
NOTE 1 - DIFFERNCE BETWEEN LISTS AND ARRAY -
1. ARRAY IS HOMGENEOUS
2. ARRAY IS MULTI DIMENSIONAL BY DEFAULT.
3. LISTS SHOW UP AS COMMA SEPARATED ITEMS. ARRAYS ARE NOT SEPERATED BY COMMAS
4. VECTORIZED CODE CAN BE WRITTEN ONLY WITH NUMPY AND NOT WITH LIST
5. COMPUTATIONS ARE FASTER IN NUMPY
6. EVERY ARITHMETIC OPERATOR DOES AN ELEMENT WISE OPERATION ON THE ARRAYS. IN LIST WE NEED TO CREATE A MAP AND LAMBDA COMBINATION TO ACHIEVE THE SAME THING.
7. The following ways are commonly used:

np.ones(): Create an array of 1s
np.zeros(): Create an array of 0s
np.random.random(): Create an array of random numbers between 0 and 1
np.arange(): Create an array with increments of a fixed step size
np.linspace(): Create an array of fixed length

'''
#NOTE : 1. ARRAY CREATION
import numpy as np
mylist=[1,2,3,4]
print (mylist)
x = np.array(mylist)
print (x)
y = np.array([[4,5,6], [7,8,9], [10,11,12]])

print (y)

# just size - two dimensional array.
np.ones([3,13])
# 4 dimensional array.
np.ones((3,3,3,4), dtype = np.int)

#random number between 0 to 1. Is useful for probabilities.
np.random.random((4,5))
#gives one dimensional array only.
np.arange(2,10,2)
np.linspace(4,40,100)
#any size
np.full((3,4),5)
np.eye(5,4, dtype = np.int)
#second parameter is the number of repitition in row and column. if one number it will repeat only in the row.
np.tile (mylist,10)

'''
checkered tiled matrix based on the entries
'''
# Read the variable from STDIN
import numpy as np
n = int(input())
checker_unit = np.array([[0,1],[1,0]])
#tile first arranges the array as per the size given, and then it repeats it.
print(np.tile(checker_unit, (int(n/2),int(n/2))))

#lowest number, highest number,  size
np.random.randint(2,20,(3,4))


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
#The out put of range and arange are same. Only that arange returns a numpy array. Here i dont know number of elements.
#in arange i know the interval. inlinspace, i dont know the interval. I just mention how many elements i need between two limits.
import numpy as np
a = np.arange(0,30,2)
a1 = list(range(0,30,2))
print (a)
print (a1)
b = np.linspace (0,4,20)
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
