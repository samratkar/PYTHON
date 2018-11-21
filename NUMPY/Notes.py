** AXIS **
Axes are defined for arrays with more than one dimension. A 2-dimensional array has two corresponding axes: the first running vertically downwards across rows (axis 0), and the second running horizontally across columns (axis 1).

Many operation can take place along one of these axes. For example, we can sum each row of an array, in which case we operate along columns, or axis 1:

>>>
>>> x = np.arange(12).reshape((3,4))

>>> x
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

>>> x.sum(axis=1)
array([ 6, 22, 38])

import numpy as np
# Dont do this
a = np.random.randn(5);
#always give all dimension details.
a = np.random.randn(5,1);
print (a);
print (a.shape);
#dont use matrix 
b = np.matrix([[1, 2, 3], [4, 5, 6]]);
print (b);
print ("b[0]=", b[0]);
print (b.shape);
#This is the way to define a given size for an array.
c = np.zeros((3,4,5));
print (c);


** WHY NUMPY **
The normal functions of Python are such that they take numbers as their inputs. But in deep learning we need inputs as matrices and arrays. So, we use numpy as it abstracts those details.

** NORM **
numpy.linalg.norm¶

numpy.linalg.norm(x, ord=None, axis=None, keepdims=False)[source]
Matrix or vector norm.

This function is able to return one of eight different matrix norms, or one of an infinite number of vector norms (described below), depending on the value of the ord parameter.

Parameters:
x : array_like
Input array. If axis is None, x must be 1-D or 2-D.
ord : {non-zero int, inf, -inf, ‘fro’, ‘nuc’}, optional
Order of the norm (see table under Notes). inf means numpy’s inf object.
axis : {int, 2-tuple of ints, None}, optional
If axis is an integer, it specifies the axis of x along which to compute the vector norms. If axis is a 2-tuple, it specifies the axes that hold 2-D matrices, and the matrix norms of these matrices are computed. If axis is None then either a vector norm (when x is 1-D) or a matrix norm (when x is 2-D) is returned.
keepdims : bool, optional
If this is set to True, the axes which are normed over are left in the result as dimensions with size one. With this option the result will broadcast correctly against the original x.
New in version 1.10.0.
Returns:
n : float or ndarray
Norm of the matrix or vector(s).

∥x∥=np.linalg.norm(x,axis=1,keepdims=True)

** RESHAPE WITH A -1 **
A trick when you want to flatten a matrix X of shape (a,b,c,d) to a matrix X_flatten of shape (b ∗ c ∗ d, a) is to use:
X_flatten = X.reshape(X.shape[0], -1).T      # X.T is the transpose of X

That is doing a -1 makes the column as product of all other dimensions of the parent array. We are doing a transpose to reverse itself. That is cool you see!

Example -
import numpy as np
a = np.random.randn(3,4,5);
print ("shape of a : ", a.shape)
a_reshaped = a.reshape(a.shape[0],-1)
print ("shape of reshaped_a:", a_reshaped.shape)
a_reshaped = a.reshape(a.shape[1],-1)
print ("shape of reshaped_a:", a_reshaped.shape)
a_reshaped = a.reshape(a.shape[2],-1)
print ("shape of reshaped_a:", a_reshaped.shape)

#Example for 1-a square
import numpy as np
b = np.random.randn(3,4)
print (b)
print (np.power(b,2))
print (1-np.power(b,2))

#Example for layer_sizes
import numpy as np
a = np.random.randn(3,1)
b = np.random.randn(3,2)
print (layer_sizes(X,Y))
