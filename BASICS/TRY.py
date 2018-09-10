#Unlike C, python does not convert automatically the character to ascii number.
import numpy as np
try:
    data = input ("Enter name")
    numeric_data = int(data)
except:
    numeric_data = -1
print (numeric_data)

np.arange(5)
