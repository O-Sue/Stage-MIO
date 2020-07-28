#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:40:20 2020

@author: utilisateur
"""

from scipy.io import loadmat
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, atan2, radians
#from matplotlib.pyplot import savefig
import pandas as pd

corr=[]
matmoy =[]
transchoice = [1]#,2,3,4,5,6,7,8,9,10,11,12,13]
axes = plt.gca()
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
            
            s=sum(xL)
            
            
            
            
        for i  in range (len(xL)-1):       #pas besoin de recréer une liste
            
            xL[i+1]=xL[i]+xL[i+1]
            
            
        for i in range (len(lat)): 
            
            W=w[i]
        
            W = W[~pd.isnull(W)]          # Ne prend pas en compte les "nan"

            s=sum(W)/len(W)
    
            matmoy.append(s)
            


        for i in range(len(matmoy)):
            
            corr.append(w[i]-matmoy[i])
            
            

plt.subplot(2, 2, 1)
        

mymap=Basemap(projection='merc',llcrnrlat=41,urcrnrlat=44,llcrnrlon=5,urcrnrlon=10,resolution='h')

X, Y = mymap(lon, lat)
mymap.scatter(X, Y, s=0.1)   #trace le transect
mymap.drawcoastlines()
myparallels=np.arange(-90,90+1,1)  
mymeridians = np.arange(-180,180+1,1) 
mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=10)
mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=10)
plt.ylabel("Lat", size = 12)
plt.xlabel("Lon", size = 12)
mymap.fillcontinents(color='0.83',lake_color='0.83',zorder=100)


plt.subplot(3, 2, 5)
        
corr2=np.transpose(corr) 
s2,depth2=np.meshgrid(xL, depth)
c=plt.pcolormesh(s2,depth2, corr2)
plt.gca().invert_yaxis()  
plt.clim(-0.15,0.10) 
plt.colorbar(aspect=10)
plt.xlabel("w corrigé de la moyenne verticale", size = 12,)
plt.gcf().subplots_adjust(left = 0.1, bottom = 0.1,right = 0.9, top = 1, wspace = 0.5, hspace = 0.3)
        
        
plt.subplot(3, 2, 2)

plt.gcf().subplots_adjust( top = 1, bottom = 0.4, wspace = 0.3)
u2=np.transpose(u)                 
a=plt.pcolormesh(s2,depth2, u2) 
plt.gca().invert_yaxis() 
plt.gca().xaxis.set_visible(False)  ####Cache que axe des abcisses !
#plt.axis('off')
plt.gcf().set_size_inches(15, 8)   ###taille figure 
plt.clim(-0.5,0.5)  
plt.colorbar(aspect=10) 
plt.ylabel("depth (m)", size = 14)


plt.subplot(3, 2, 4)

plt.gcf().subplots_adjust(bottom = 0, right = 1,left = 0.1)
v2=np.transpose(v) 
b=plt.pcolormesh(s2,depth2, v2)
plt.gca().invert_yaxis() 
plt.colorbar(aspect=10) 
plt.clim(-0.5,0.5) 
plt.gca().xaxis.set_visible(False)

        
plt.subplot(3, 2, 6)

w2=np.transpose(w) 
c=plt.pcolormesh(s2,depth2, w2)
plt.gca().invert_yaxis()  
plt.colorbar(aspect=10) 
plt.clim(-0.5,0.5) 
#plt.colorbar(aspect=17,shrink=0.6, orientation="horizontal", pad=0.5)   
plt.xlabel("longueur du transect (Km)", size = 14)
        
#plt.subplot(4, 2, 8)       (si on veut isoler une unique colorbar)
#plt.axis('off')
#plt.colorbar(aspect=17,orientation="horizontal", label=  "vitesse du courant en m/s")#shrink=0.8, orientation="horizontal", )



#savefig('Y'+ str(p) +'.png', bbox_inches='tight')