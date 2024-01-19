import math
import numpy as np
import matplotlib.pyplot as plt

g = 10
m= 10
c = 50
time = np.linspace(0,2,1000)

vt = int((g*m)/c)
v2 = vt*(1-math.e**(-(c/m)**time))
plt.plot(time,v2)

print(v2)

plt.title('Velocity of a Falling Body')
plt.xlabel("Time (s)")
plt.ylabel('Velocity (m/s)')
plt.legend()

plt.show()