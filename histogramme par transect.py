#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:18:54 2020

@author: utilisateur
"""



import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
#from matplotlib.pyplot import savefig
import pandas as pd


matmoy2 =[]
b=[]
corr=[]
matmoy =[]
transchoice = [2]#,2,3,4,5,6,7,8,9,10,11,12,13]

axes = plt.gca()

for p in transchoice:

        x = loadmat('T'+ str(p) +'.mat')

        lon = x['lon']
        lat = x['lat']
        u = x['u']
        v = x['v']
        w = x['w']
        depth=x['depth']
        


        for i in range (len(lat)): 
            
            
            W=w[i]
            
            W = W[~pd.isnull(W)]   #### Ne prend pas en compte les "nan"
            
            s=sum(W)/len(W)
            
            matmoy.append(s)
            
        
        for j in range (len(matmoy)):
            
                     
                                 corr.append(w[j]-matmoy[j])
                 

        b=np.asarray(corr)    # arrange la liste de array (corr) en matrice
        
        for i in range (b.shape[0]): 

                 for k in range (b.shape[1]):
                
                         matmoy2.append(b[i, k])    
      
                    

        plt.hist(matmoy2 , bins=200,range = (-0.2, 0.2))



        #savefig('D'+ str(p) +'.png', bbox_inches='tight')



