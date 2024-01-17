import matplotlib.pyplot as plt
import numpy as np
import math


#variables
no = 500
time = np.linspace(0,60,50)
lams = [0.1,0.35,0.75,1]
for i in lams:
    numbers = no*math.e**(-i*time)
    plt.plot(time,numbers, label = 'λ = '+ str(i))





#plot formatting

plt.title('Radioactive Decay with Varying λ')
plt.xlabel("Time (s)")
plt.ylabel('Number of Radioactive Atoms')
plt.legend()

#show plot
plt.show()

#save plot