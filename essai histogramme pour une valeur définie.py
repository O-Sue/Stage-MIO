#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:10:31 2020

@author: utilisateur
"""




from scipy.io import loadmat
import matplotlib.pyplot as plt
import pandas as pd
#from matplotlib.pyplot import savefig


corr=[]
matmoy =[]
transchoice = [2]#,2,3,4,5,6,7,8,9,10,11,12,13]

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
        
            W = W[~pd.isnull(W)]  

            s=sum(W)/len(W)
            
            matmoy.append(s)
            




        for j in range(x): ### 'x' compris dans len(matmoy)):    ####  valeur j que l'on veut plotter indep
            
                 a=w[j]-matmoy[j]
                 
                 



        plt.hist(a, bins=60,range = (-0.2, 0.2))
        
        #savefig('C'+ str(p) +'.png', bbox_inches='tight')
