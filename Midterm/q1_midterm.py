#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:40:48 2021

@author: gursehajharika
"""

import numpy as np
import math
import os 



def PrintMatrix(name,x):
    print
    print(name,"=")
    print(x)





x = np.loadtxt('data10.txt', delimiter=' ')
euc = []

NumData = x[:,1:4]
maxNumData = np.max(NumData,axis = 0)
minNumData = np.min(NumData,axis = 0)
NumData = (NumData - minNumData)/(maxNumData - minNumData)

print (NumData)
eucli  = x[:,:3]
print (eucli)

C1 = eucli[:,0]-min(eucli[:,0])
C1 = C1/max(C1)

C2 = eucli[:,1]-min(eucli[:,1])
C2 = C2/max(C2)

C3 = eucli[:,2]-min(eucli[:,2])
C3 = C3/max(C3)


DNumE = np.mat(np.zeros((10,2)))
print (DNumE)


        
for i in range(10):
    for j in range(2):
        for k in range(4):
            DNumE[i,j] = DNumE[i,j] + (NumData[i,k]-NumData[j,k])**2.0
           # DNumM[i,j] = DNumM[i,j] + abs(NumData[i,k]-NumData[j,k])
           # DMax[k] = abs(NumData[i,k]-NumData[j,k])
        DNumE[i,j] = (DNumE[i,j])**0.5
        #DNumMax[i,j] = max(DMax)



PrintMatrix("Euclidean Distance",DNumE)
#PrintMatrix("Manhattan Distance",DNumM)
#PrintMatrix("Supremum Distance",DNumMax)
