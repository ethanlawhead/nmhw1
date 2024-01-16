import matplotlib.pyplot as plt
import numpy as np
import math


#variables
no = 1000
time = range(0, 4)
lams = [0.01,0.1,1,10]
numbers = no*math.e**(-0.1)
plt.plot(time,lams)





#plot formatting

plt.title('Radioactive Decay with Varying λ')
plt.xlabel("Time (s)")
plt.ylabel('Number of Radioactive Atoms')
plt.legend()
#show plot
plt.show()

#save plot