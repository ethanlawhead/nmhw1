import matplotlib.pyplot as plt
import numpy as np
import math


#variables
no = 1000
lams = [0.01,0.1,1,10]

plt.plot(no*math.e**(-0.01))





#plot formatting

plt.title('Radioactive Decay with Varying λ')
plt.xlabel("Time (s)")
plt.ylabel('Number of Radioactive Atoms')
plt.legend()
#show plot
plt.show()

#save plot