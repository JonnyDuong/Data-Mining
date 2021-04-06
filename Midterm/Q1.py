# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:06:12 2021

@author: jonat
"""
import numpy as np
from operator import itemgetter
import math
#Q1 -------------------------------------------------------------------------------------------------------------------------
x = np.loadtxt('data10.txt', delimiter=' ')
num_euc = []
num_man = []
num_sup = []
nom_man = []
bin_dis = []

num_mean0 = []
num_std0 = []
num_mean1 = []
num_std1 = []

sorted_man=[]

# print(x)
num = x[:,:3]
# print(numeric.shape)
nom = x[:,3:6]
# print(nom)
binary = x[:,6:-1]
# print(binary)
num_adj = []

C1 = num[:,0]-min(num[:,0])
C1 = C1/max(C1)
# print(C1)
num_adj = np.append(num_adj,C1)

C2 = num[:,1]-min(num[:,1])
C2 = C2/max(C2)
num_adj = np.append(num_adj,C2)
num_adj = np.reshape(num_adj,(2,10))
num_adj = num_adj.T
# print(C2)
# print(num_adj)

# print(num_adj[:,0]-C1)
# print(num_adj[:,1]-C2)

C3 = num[:,-1]-min(num[:,-1])
C3 = C3/max(C3)
C3 = np.reshape(C3,(10,1))
# print(C3)
num_adj = np.append(num_adj,C3,1)
# print(num_adj)

for q in range(len(num_adj)):
    for w in range(len(num_adj)):
        diff_euc = np.linalg.norm(num_adj[q] - num_adj[w])
        diff_man = num_adj[q] - num_adj[w]
        diff_sup = max(abs(diff_man))
        diff_man = sum(abs(diff_man))
        
         
        num_euc = np.append(num_euc,diff_euc)
        num_man = np.append(num_man,diff_man)
        num_sup = np.append(num_sup,diff_sup)
        
num_euc = np.reshape(num_euc,(10,10))
num_man= np.reshape(num_man,(10,10))
num_sup = np.reshape(num_sup,(10,10))

# print(num_euc)

for e in range(len(nom)):
    for r in range(len(nom)):
        nom_man = np.append(nom_man,(3-np.sum(nom[e]==nom[r]))/3)
        
nom_man = np.reshape(nom_man,(10,10))

for t in range(len(binary)):
    for y in range(len(binary)):
        bin_dis = np.append(bin_dis,(np.sum(binary[t]!=binary[y]))/3)
bin_dis = np.reshape(bin_dis,(10,10))

 
total = np.add(3*num_euc,3*nom_man)
total = np.add(total,3*bin_dis)/9

#Q2 K-Nearest neighbour -----------------------------------------------------------------------------------------------------
total_man = np.add(3*num_man,3*nom_man)
total_man = np.add(total,3*bin_dis)/9

classify= [[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]]
classify = np.append(total_man,classify,1)

for z in range(10):
    column_sort = np.sort(total_man[:,z])
    sorted_man = np.append(sorted_man,column_sort)
sorted_man = np.reshape(sorted_man,(10,10))
sorted_man = sorted_man.T
sorted_mant = sorted_man[1:,:]

for z in range(10):
    for k in range(3,8,2):
        neighbours = sorted_mant[:k,z]
        # print(neighbours)
    

#Q3 Bayesian ----------------------------------------------------------------------------------------------------------------
class_0 = num_adj[:5,:]
class_1 = num_adj[5:,:]
data = num_adj

for z in range(3):
    class_0_num = class_0[:,z]
    class_1_num = class_1[:,z]
    
    class0_mean = np.mean(class_0_num)
    class0_std = np.std(class_0_num)
    
    class1_mean = np.mean(class_1_num)
    class1_std = np.std(class_1_num)
    
    num_mean0 = np.append(num_mean0,class0_mean)
    num_std0 = np.append(num_std0,class0_std)
    
    num_mean1 = np.append(num_mean1,class1_mean)
    num_std1 = np.append(num_std1,class1_std)
    

for y in range(3):
    for z in range(10):
        pdf_num0 = (1/math.sqrt(2*math.pi)*num_std0[y])*math.exp(-1*((data[z,y]-num_mean0[y])/2*(num_std0[y]**2)))
        pdf_num1 = (1/math.sqrt(2*math.pi)*num_std1[y])*math.exp(-1*((data[z,y]-num_mean1[y])/2*(num_std1[y]**2)))
        # print(z,'\t','Class 0:',pdf_num0,'\t','Class 1:',pdf_num1)
