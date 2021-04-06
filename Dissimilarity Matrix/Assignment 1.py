# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:35:17 2021

@author: jonat
"""

import pandas as pd
from operator import itemgetter
import numpy as np
import math

def main():
    data_pd = pd.read_excel('Numeric Data Q1.xlsx')
    data_np = pd.DataFrame.to_numpy(data_pd)
    data_num = data_np[:,:6]
    data_bin = data_np[:,6:]
    # print(data_bin.size)
    # print(data_num)
    min_array = []
    max_array = []
    euclidean = []
    manhattan = []
    supremum = []
    dis_bin = []
    s_max = 0
    min_values = np.empty(1)
    
    #Q1
    for x in range (6):
        data_num = sorted(data_num,key=itemgetter(x))
        # print(data_num)
        min_array = np.append(min_array,data_num[0],axis = 0)
        max_array = np.append(max_array,data_num[9],axis = 0)
        
    min_array = np.reshape(min_array,(6,6))
    max_array = np.reshape(max_array,(6,6))
    # print(min_array.diagonal())
    min_values = min_array.diagonal()
    max_values = max_array.diagonal()
    # print(min_values)
    # print(min_values,'\n',max_values)
    #77,219,75,155,92,91
    
    data_less = data_num - min_values
    # print(data_less)
    data_div = data_num/max_values
    # print(data_div)
    
    for x in range (10):
        for y in range (10): 
            test = data_div[x] - data_div[y] 
            # print(test)
            test_max = abs(max(test))
            # print(test_max)
            if test_max>=s_max:
                s_max = test_max
            else:
                s_max = s_max
                
            test = sum(np.square(test))
            test = np.sqrt(test)
            
            m_test = abs(data_div[x] - data_div[y])
            m_test = sum(m_test)
               
            euclidean = np.append(euclidean,test)
            manhattan = np.append(manhattan,m_test)
            supremum = np.append(supremum,s_max)
            
        # print(test)    
    euclidean = np.reshape(euclidean,(10,10))
    manhattan = np.reshape(manhattan,(10,10))
    supremum = np.reshape(supremum,(10,10))
    print('Euclidean','\n',euclidean)
    # print('Manhattan','\n',manhattan)
    # print('Supremum', '\n',supremum)
    
    #Q2
    for x in range (10):
        for y in range(10):
            diff = abs(data_bin[x]-data_bin[y])
            z = sum(diff)
            z = format(z/6,'.2f')
            dis_bin = np.append(dis_bin,z)
            
    dis_bin = np.reshape(dis_bin,(10,10))    
    # print(dis_bin)
    
    #Q3
    # euc = np.add(euclidean + dis_bin)
    # man = np.add(manhattan + dis_bin)
    # sup = np.add(supremum + dis_bin)
    
    
def table2():
    ord_diss = []
    data_t2 = pd.read_excel('Table 2.xlsx')
    data = pd.DataFrame.to_numpy(data_t2)
    data = data[2:,:]
    # print(t2_pd)
    c = (data[:,:3])/5
    # print(c)
    for x in range (10):
        for y in range (10):
            diff = format(abs(sum(c[x]) - sum(c[y])),'.1f')
            # print(diff)
            ord_diss = np.append(ord_diss,diff)
    ord_diss.reshape((10,10))
    # print(ord_diss)
    
    data_nom = data[:,3:]
    # print(data_nom)
#Q5 count number of dissasimilarities between each data point. divide by 6 to get difference. Compare all data points
#Q6 sum tables in Q5 and Q4
main()
table2()
    