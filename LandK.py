# -*- Lock and key -*-
"""
Created on Tue Feb 14 17:49:46 2023

@author: danev
"""

import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation

betaK = 0.5  # relative speed of the lock in keys reference

for i in range(-25,50,1)   :
    tau = i/10       # time in light seconds

    gamma = 1/(np.sqrt(1-(pow(betaK,2))))  # gamma factor of L in K
    a = 1  # width of key and arms (y direction)
    l = 2  # lenght of key at rest
    h = 1 #lenght of arm at rest
    d = 2  # depth of lock at rest
    b= 1   # thickness of back of lock at rest
    x1 = 0
    x2 = -l
    x3 = -l-h
    x4 =-1*betaK*tau   #x4 at time tau in keys reference frame
    x5 = (d/gamma)-betaK*tau  #x5 at time tau in K
    x6 = (d+b/gamma)-betaK*tau  #x6 at tau in K

    print("gamma = " ) 
    print ("x1 =")
    print(x1)
    print(x4)
    print("x5 = ")
    print(x5)
    print(x6)

    KKx = np.array([x1,x2,x2,x3,x3,x2,x2,x1,x1]) #x coords of the key in its frame
    KKy = np.array([0,0,-a,-a,2*a,2*a,a,a,0])  #y coords of the key in its frame

    LKx = np.array([x4,x4,x6,x6,x4,x4,x5,x5,x4])
    LKy = np.array([0,-a,-a,2*a,2*a,a,a,0,0])

    print(KKx)
    print(KKy)
    plt.plot(LKx,LKy)
    plt.plot(KKx,KKy)
    plt.xlim([-4,4])
    plt.show()
    if x1 > x5 or x2 >= x4 :
        print (x2,x4)
        break
    
        
