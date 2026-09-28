# -*- Lock and key -*-
"""
Created on Tue Feb 14 17:49:46 2023

@author: danev
"""

import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation

betaK = 0.6  # relative speed of the lock in keys reference
gamma = 1/(np.sqrt(1-(pow(betaK,2))))  # gamma factor of L in K
a = 1  # width of key and arms (y direction)
l = 40  # lenght of key at rest
h = 10 #width of arm at rest
d = 60  # depth of lock at rest
b= 10   # thickness of back of lock at rest
tauL24 = l/(gamma*betaK)
tauL15 = d/betaK
tauL73 = ((l/(gamma*betaK))+(l+h)/gamma)*(1/(betaK+1))
tauL81 = ((-1*l)/(gamma*betaK))*(1/(betaK-1))
tauL96 = b+(d/betaK)
tauL104 = d+(d/betaK)
tauL102 = (d+d/betaK+l/gamma)*(1/(betaK+1))
tauL103 = (d+d/betaK+(l+h)/gamma)*(1/(betaK+1))
tauL85 = d+l/(gamma*betaK)
tau86 = d+b+l/(gamma*betaK)

Ey = np.array([0.5,0.5])

numSteps = int(round(150))  #nember of itterations 
dtau = 1# time steps in tau 
# dtau and numSteps are adjusted by 1/betaK so that the model runs at a simillar speed
# and for long enough at low and high BetaK
for i in range(0,numSteps,dtau)   :
    tau = i      # time in light seconds
    print(tau)
    print("tau15=",tauL15)
    print("tau24=", tauL24)
    print("tau81=", tauL81)
    
# x values of points in L
    x1L = betaK*tau
    x2L = -1*(l/gamma)+betaK*tau
    x3L = -1*((l+h)/gamma)+betaK*tau
    x4L = 0
    x5L = d
    x6L = d+b
    print ("l=", x1L-x2L)
    x24L=0
    x15L=d
    
    x7L = (x24L)-(tau-tauL24) #signal sent from 24 to 3
    x8L = (x24L)+(tau-tauL24) #signal sent from 24 to 1 and 6 also x9S-
    x9L = (x15L)+(tau-tauL15)
    x10L = (x15L)-(tau-tauL15)
    
    #stop conditions
    if tauL15<tauL24:
        if tau>=tauL15  : 
            x1L = betaK*tauL15
        if tauL104>=tauL24:
            if tau>=tauL24:
                x2L = -1*(l/gamma)+betaK*tauL24
            if tau>=tauL73:
                x3L = -1*((l+h)/gamma)+betaK*tauL73
        if tauL24>tauL104:
            if tau>=tauL102:
                x2L = -1*(l/gamma)+betaK*tauL102
            if tau>=tauL103:
                x3L = -1*((l+h)/gamma)+betaK*tauL103
    if tauL24<tauL15:
        if tau>=tauL24:
            x2L = -1*(l/gamma)+betaK*tauL24
        if tauL15<=tauL81: 
            if tau>=tauL15:
                x1L = betaK*tauL15
        if tauL15>=tauL81:
            if tau>=tauL81:
              x1L = betaK*tauL81  
        if tau>=tauL73:
            x3L = -1*((l+h)/gamma)+betaK*tauL73
            
 
    
    
   
   
    
    
    KLx = np.array([x1L,x2L,x2L,x3L,x3L,x2L,x2L,x1L,x1L])
    KLy = np.array([0,0,-a,-a,2*a,2*a,a,a,0])
    
    LLx = np.array([x4L,x4L,x6L,x6L,x4L,x4L,x5L,x5L,x4L])
    LLy = np.array([0,-a,-a,2*a,2*a,a,a,0,0])
   
    fig, axis = plt.subplots() #set up figure
    plt.text(0,2.25,"L")
    plt.text(x3L-6,-1,'x3')
    plt.text(x2L,-1,'x2')
    plt.text(x1L,0.1,'x1')
   
    plt.text(x4L,1.1,'x4')
    plt.text(x5L-2,1.1,'x5')
    plt.text(x6L-2,2,'x6')
    
    plt.text(0,-1.51,'tau:')
    plt.text(0,-1.7, tau)
    axis.plot(LLx,LLy) # plot lock in locks frame lower
    axis.plot(KLx,KLy) # plot key in locks frame lower
    
    if tauL24<tauL102:
        if tau>=tauL24:
            E7x = np.array([x24L,x7L])
            E8x = np.array([x24L,x8L])
       
        
        
            axis.plot(E7x,Ey)
            axis.plot(E8x,Ey)
    if tauL15<tauL81:
        if tau>=tauL15:
            E9x = np.array([x15L,x9L])
            E10x = np.array([x15L,x10L])
       
       
        
            axis.plot(E9x,Ey)
            axis.plot(E10x,Ey)     
    axis.set_xlim([(-1*l)-2,d+b+2])
    
    # x axis limited as a functions of l and d so it auto corrects to given inputs
    
    plt.show()
    
 
        
