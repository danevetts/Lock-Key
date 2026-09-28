# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:24:13 2023

@author: danev
"""

import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation

betaK = 0.6  # relative speed of the lock in keys reference
gamma = 1/(np.sqrt(1-(pow(betaK,2))))  # gamma factor of L in K
a = 1  # width of key and arms (y direction)
l = 40  # lenght of key at rest
h = 10 #lenght of arm at rest
d = 60  # depth of lock at rest
b= 10   # thickness of back of lock at rest

Ey = np.array([0.5,0.5])

x24K=-l
x15K=0
tauK15 = d/(gamma*betaK)
tauK24 = l/betaK
tauK73 = x24K+tauK24+l+h
tauK81 = tauK24-x24K
tauK96 = (((d+b)/gamma)+tauK15)/(betaK+1)
tauK104 = (x15K+tauK15)/(1-betaK)
tauK102 = x15K+tauK15+l
tauK103 =  x15K+tauK15+l+h
tauK85 = (x24K-tauK24-(d/gamma))/(-betaK-1)
tauK86 = (x24K-tauK24-((d+b)/gamma))/(-betaK-1)
numSteps = int(round(150))  #nember of itterations 
dtau = int(round(1))# time steps in tau 
# dtau and numSteps are adjusted by 1/betaK so that the model runs at a simillar speed
# and for long enough at low and high BetaK
for i in range(0,numSteps,dtau)   :
    tau = i      # time in light seconds
    # x values of points in K
    x1k = 0
    x2k = -l
    x3k = -l-h
    x4k =-1*betaK*tau   #x4 at time tau in keys reference frame
    x5k = (d/gamma)-betaK*tau  #x5 at time tau in K
    x6k = ((d+b)/gamma)-betaK*tau  #x6 at tau in K
    
    print ("k = ", x5k-x4k)
    x24K=-l
    x15K=0
    
    x7K = (x24K)-(tau-tauK24) #signal sent from 24 to 3
    x8K = (x24K)+(tau-tauK24) #signal sent from 24 to 1 and 6 also x9S
    x9K = (x15K)+(tau-tauK15)
    x10K = (x15K)-(tau-tauK15)
    
    print(tau)
    print("tau15=",tauK15)
    print("tau24=",tauK24)
    print("tau104=",tauK104)
    print("tau96=", tauK96)
    print("tau86=", tauK86)
    if tauK15<=tauK24:
        if tau>=tauK15  : 
            x5k = (d/gamma)-betaK*tauK15
        if tauK104>=tauK24:
            if tau>=tauK24:
                x4k = -1*betaK*tauK24
            
        if tauK24>tauK104:
            if tau>=tauK104:
                x4k = -1*betaK*tauK104
        if tau>=tauK96:
            x6k = ((d+b)/gamma)-betaK*tauK96
    if tauK24<=tauK15:
        if tau>=tauK24:
            x4k = -1*betaK*tauK24
        if tauK15<=tauK85: 
            if tau>=tauK15:
                x5k = (d/gamma)-betaK*tauK15
            if tau>=tauK96:
                x6k = ((d+b)/gamma)-betaK*tauK96
        if tauK15>=tauK85:
            if tau>=tauK85:
              x5k = (d/gamma)-betaK*tauK85 
            if tau>=tauK86:
                x6k =((d+b)/gamma)-betaK*tauK86
         
         
    KKx = np.array([x1k,x2k,x2k,x3k,x3k,x2k,x2k,x1k,x1k]) #x coords of the key in its frame
    KKy = np.array([0,0,-a,-a,2*a,2*a,a,a,0])  #y coords of the key in its frame
         
    LKx = np.array([x4k,x4k,x6k,x6k,x4k,x4k,x5k,x5k,x4k]) #x coords of lock in K frame
    LKy = np.array([0,-a,-a,2*a,2*a,a,a,0,0])#y coords of lock in K frame
         
    fig, axis = plt.subplots() #set up figure
    plt.text(0,2.25,"K")
    plt.text(x3k-6,-1,'x3')
    plt.text(x2k,-1,'x2')
    plt.text(x1k,0.1,'x1')
    plt.text(x4k,1.1,'x4')
    plt.text(x5k-2,1.1,'x5')
    plt.text(x6k-2,2,'x6')
    plt.text(0,-1.51,'tau:')
    plt.text(0,-1.7, tau)
    axis.plot(LKx,LKy) # plot lock in locks frame lower
    axis.plot(KKx,KKy) # plot key in locks frame lower
    
    if tauK24<tauK102:
        if tau>=tauK24:
            E7x = np.array([x24K,x7K])
            E8x = np.array([x24K,x8K])
       
        
        
            axis.plot(E7x,Ey)
            axis.plot(E8x,Ey)
          
    if tauK15<tauK81:
        if tau>=tauK15:
            E9x = np.array([x15K,x9K])
            E10x = np.array([x15K,x10K])
       
       
        
            axis.plot(E9x,Ey)
            axis.plot(E10x,Ey)     
    axis.set_xlim([(-1*l-h)-2,d+b+2])
    plt.show()