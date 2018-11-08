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
