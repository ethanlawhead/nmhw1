import matplotlib.pyplot as plt
import numpy as np
import math


#variables
no = 500
time = np.linspace(0,20,50)
lams = [0.1,0.35,0.75,1]
for i in lams:
    numbers = no*math.e**(-i*time)
    plt.plot(time,numbers, label = 'λ = '+ str(i))

    plt.text(time[-1]/8,(no*np.exp(-i*(time[-1])/8)),'λ = '+ str(i))



#plot formatting

plt.title('Radioactive Decay with Varying λ')
plt.xlabel("Time (s)")
plt.ylabel('Number of Radioactive Atoms')
plt.legend()

#save plot
plt.savefig('decay.png')

#show plot
plt.show()
