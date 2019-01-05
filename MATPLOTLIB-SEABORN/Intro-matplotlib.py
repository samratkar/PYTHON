import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#lower limit 5, upper limit 99, number of points 100.
x = np.linspace(5,100,15)
y = np.linspace(10,1000,100)
plt.xlabel("Current")
plt.ylabel("Voltage")
plt.title("Ohmns Law")
plt.xlim(20,80)
plt.ylim(200,800)
plt.plot(x,y,'r-')
plt.show()

#MULTIPLE GRAPHS
x = np.linspace(0, 5, 10)
y = np.linspace(3, 6, 10)

# plot three curves: y, y**2 and y**3 with different line types
plt.plot(x, y, 'r-', x, y**2, 'b+', x, y**3, 'g^')
plt.show()

#####
#NOTE: SUBPLOT - Figures are an array of plots.
x = np.linspace(1,10,100)
y = np.log(x)
#Initiate a new figure explicitly.
plt.figure(1)

#Create a subplot with one row and two columns
plt.subplot(121)
plt.plot(x,y)
plt.subplot(122)
plt.plot(x,y**2)
plt.subplot(10,10,1)
plt.plot(x,y)
plt.subplot(10,10,2)
plt.plot(x,y**2)
