import math
import numpy as np
import matplotlib.pyplot as plt

#initial variables
g = 10
m= 10
c = 50
delt = 0.1

time = np.linspace(0,2,100)
time2 = np.arange(0,2.1,delt)
#function for terminal velocity
def vt(gravity,mass,drag):
    vt = int((g*m)/c)
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
# def eq3(vi,g,c,m,t,delt):
#     for i in t:
#         v = vi+(g-(c/m)*vi)*delt
#         vi = v
#     plt.plot(t,v)
#     return v

#part a
va = vt(g,m,c)

y_valeq3 = eq3(0,g,c,m,delt,time2)

v2 = va*(1-math.e**(-(c/m)*time))
print(1-math.e**(-(c/m)*time))
plt.plot(time,v2)
plt.plot(time2,y_valeq3)



#plot formatting
plt.title('Velocity of a Falling Body')
plt.xlabel("Time (s)")
plt.ylabel('Velocity (m/s)')
plt.legend()

#show plot
plt.show()

