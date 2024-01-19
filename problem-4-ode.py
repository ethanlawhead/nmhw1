import math
import numpy as np
import matplotlib.pyplot as plt

#initial variables
g = 10
m= 10
c = 50
time = np.linspace(0,2,1000)

#function for terminal velocity
def vt(gravity,mass,drag):
    vt = int((g*m)/c)
    return vt
#part a
va = vt(g,m,c)

v2 = va*(1-math.e**(-(c/m)**time))
plt.plot(time,v2)

#plot formatting
plt.title('Velocity of a Falling Body')
plt.xlabel("Time (s)")
plt.ylabel('Velocity (m/s)')
plt.legend()

#show plot
plt.show()