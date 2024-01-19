import math
import numpy as np
import matplotlib.pyplot as plt

#initial variables
g = 10
m1= 10
c = 50
delt = 0.1

time = np.linspace(0,2,100)
time2 = np.arange(0,2.1,delt)
#function for terminal velocity
def vt(gravity,mass,drag):
    vt = int((gravity*mass)/drag)
    return vt

def eq3(vi,g,c,m,delt,t):
    eqlst = []
    for i in t:
       if i == 0:
           v = 0
       else:
        v = vi+((g-(c/m)*vi)*delt)
       
       eqlst.append(v)
       vi = v

    return eqlst

def percent(terminal, eq2, eq3):
   print('not done yet')
   

#part a
va = vt(g,m1,c)

y_valeq3 = eq3(0,g,c,m1,delt,time2)

v2 = va*(1-math.e**(-(c/m1)*time))

plt.plot(time,v2, label = 'part a')
plt.plot(time2,y_valeq3, label = 'part b')



#plot formatting
plt.title('Velocity of a Falling Body')
plt.xlabel("Time (s)")
plt.ylabel('Velocity (m/s)')
plt.legend()

#show plot
plt.show()

