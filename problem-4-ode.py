import math
import numpy as np
import matplotlib.pyplot as plt

#initial variables
g = 10
m1= 10
m2 = 100
c = 50
delt = 0.1

time = np.linspace(0,2,100)
time2 = np.arange(0,2.1,delt)

#function for terminal velocity
def vt(gravity,mass,drag):
    vt = int((gravity*mass)/drag)
    return vt

#function for eq 3
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

def max_time(vt,eq,delt):
   print('not done yet')

#function to find time for 99.99% vt
def percent(terminal, eq, time):
   
   #find 99.99% of terminal velocity
   ninety_nine = .9999 * terminal

   check = False

   #go through equation to find value and return time
   while  check == False:
        for i in eq:
            if i >= ninety_nine:
                check = True
                j = list(eq).index(i)
                print('it takes' , time[j] , 'seconds')
                break
            else:
                continue

   

#part a
va = vt(g,m1,c)


v2 = va*(1-math.e**(-(c/m1)*time))

#part b
y_valeq3 = eq3(0,g,c,m1,delt,time2)

#part c
max_time

#part d
y_vald = eq3(0,g,c,m2,delt,time2)
max_time

#part e
percent(va,v2,time)

#plotting
plt.plot(time,v2, label = 'part a')
plt.plot(time2,y_valeq3, label = 'part b')



#plot formatting
plt.title('Velocity of a Falling Body')
plt.xlabel("Time (s)")
plt.ylabel('Velocity (m/s)')
plt.legend()

#show plot
plt.show()

