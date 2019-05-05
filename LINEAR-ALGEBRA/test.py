import numpy as np
import pandas as pd

1. determining the m, n from a linear combination of a set of basis vectors.

lincom = np.array([19,29,54])
set_of_vectors = np.array([[1,2,3], [4,5,6], [1,2,6]])
np.linalg.solve(set_of_vectors, lincom)

2. Doing a Linear Transformation of a matrix of 6 vectors.  Just multiply the vectors with the transoforming vector! - ELONGATION

METHOD 1

#Let's create a dataframe matrix here to understand the effect.
a = [[1,2],[-2,3],[-2,1],[3,7],[4,5],[6,4]]
b = ['X','Y']
c = pd.DataFrame(a,columns = b)
c
## Now let's denote the linear transformation matrix.
## (2,0) and (0,1) are the vectors that would denote the columns of this matrix.
## Therefore (2,0) and (0,1) would be the rows
L = np.array([[2,0],[0,1]])
L
#Let's apply the transformation now.
#Note that we have used c.values to convert that dataframe to a numpy array
#And taken its transpose so that the transformation happens on each vector
d  = L @ (c.values).T
#Now let's show the final changed matrix by findings the transpose again.
d.T

METHOD 2

a = [[1,2],[-2,3],[-2,1],[3,7],[4,5],[6,4]]
b = ['X','Y']
c = pd.DataFrame(a,columns = b)
c
c.shape
L = pd.DataFrame([[2,0],[0,1]])
L
L.shape
#see it gives an error, as the index names are different from the columns names of the two matrices
d = c.dot(L)
# to avoid changing the index and column names, it is better to use np.dot() method. It just takes the values of the matrices without worrying about the names of the index and columns.
np.dot(c,L)
# or your can use numpy @ or matmul function to do the matrix multiplication
c.values @ L.values

3. TRANSFORMATION OF A VECTOR WITH ANOTHER MARTRIX
a = np.array([2,3])
a
b = np.array([[1,0],[0,1]])
b
lintrans = a @ b
lintrans

4.
a = np.array([[1,4],[4,2]])
a
b = np.array([[1,2],[3,4],[5,6],[7,8]])
b
lintrans = b @ a
lintrans

5. Find the eigen vector and matrix pairs
A = np.array([[2,1],[1,2]])
v = np.array([1,-1])
Av = A @ v
Av
K = np.linalg.eig(A)
K
A = np.array([[2,2],[1,2]])
v = np.array ([1,-1])
Av = A @ v
Av
K = np.linalg.eig(A)
K

A = np.array([[1,2,3],[2,3,1],[3,1,2]])
K = np.linalg.eig(A)
K

a = np.array([1,2,3])
b = np.array([2,4,2])
a @ b
np.dot(a,b)
