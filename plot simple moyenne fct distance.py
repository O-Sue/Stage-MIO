#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:26:40 2020

@author: utilisateur
"""

from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, atan2, radians
#from matplotlib.pyplot import savefig

transchoice = [1]#,2,3,4,5,6,7,8,9,10,11,12,13]
matmoy =[]

for p in transchoice:

        x = loadmat('T'+ str(p) +'.mat')

        lon = x['lon']
        lat = x['lat']
        u = x['u']
        v = x['v']
        w = x['w']
        depth=x['depth']
        
        xL=[0]
        n=0
        yL=[0]
        R = 6373.0
        
        for i in range (len(lat)-1):
            
            
            lat1 = radians(lat[n])
            lon1 = radians(lon[n])
            lat2 = radians(lat[n+1])
            lon2 = radians(lon[n+1])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c

            n=n+1

            xL.append(distance)
            
            z=sum(xL)
            
            
        for i  in range (len(xL)-1):      
            
            xL[i+1]=xL[i]+xL[i+1]
                    
            
        for i in range (len(xL)): 
            
            W=w[i]
            W = W[~pd.isnull(W)]
            s=sum(W)/len(W)
            matmoy.append(s)
           
                        
                        
        plt.figure(figsize=((8,6)))
        
        axes= plt.gca()
        plt.gca().xaxis
        plt.xlabel(xlabel="distance en km")
        plt.ylabel(ylabel="w_moy colonne d’eau en m/s")
        #plt.title("Variation de la moyenne de vitesse verticale",loc = "right" )
        axes.set_xlim(100, 150)
        plt.suptitle('Variation de la moyenne de vitesse verticale ', fontsize = 13, x = 0.5, y = 0.995)
        plt.plot(xL,matmoy)
        
        
        #savefig('Xa'+ str(p) +'.png', bbox_inches='tight')
