#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:29:04 2021

@author: i0678
"""

import yfinance as yf
import numpy as np
from sklearn.cluster import KMeans
from kneed import DataGenerator, KneeLocator
from matplotlib import pyplot as plt
import pandas as pd
from datetime import time
from itertools import chain


df = yf.download(tickers='^NSEI',start='2019-6-01', end='2020-01-01', interval ='1h')
X = np.array(df['Close'])

df['level_1'] = None

df['level_2'] = None

df['level_3'] = None

df['level_4'] = None

df['Datetime'] = pd.to_datetime(df.index)

'''    
sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X.reshape(-1,1))
    sum_of_squared_distances.append(km.inertia_)
kn = KneeLocator(K, sum_of_squared_distances,S=1.0, curve="convex", direction="decreasing")
kn.plot_knee()


kmeans = KMeans(n_clusters= kn.knee).fit(X.reshape(-1,1))
c = kmeans.predict(X.reshape(-1,1))


minmax = []
for i in range(kn.knee):
    minmax.append([-np.inf,np.inf])
for i in range(len(X)):
    cluster = c[i]
    if X[i] > minmax[cluster][0]:
        minmax[cluster][0] = X[i]
    if X[i] < minmax[cluster][1]:
        minmax[cluster][1] = X[i]
        
    
for i in range(len(X)):
    colors = ['b','g','r','c','m','y','k','w']
    c = kmeans.predict(X[i].reshape(-1,1))[0]
    color = colors[c]
    plt.scatter(i,X[i],c = color,s = 1)
    
for i in range(len(minmax)):
    plt.hlines(minmax[i][0],xmin = 0,xmax = len(X),colors = 'g')
    plt.hlines(minmax[i][1],xmin = 0,xmax = len(X),colors = 'r')
'''

level_1 = None
level_2 = None
level_3 = None
level_4 = None
    
for index in range(101, len(df)):

    if df.iloc[index]['Datetime'].time() == time(hour=9, minute=15):
        curr_df = df[index-100: index].copy()
        X = np.array(curr_df['Close'])
        kmeans = KMeans(n_clusters= 4).fit(X.reshape(-1,1))
        c = kmeans.predict(X.reshape(-1,1))
        minmax = []
        for i in range(4):
            minmax.append([np.inf,-np.inf])
        for i in range(len(X)):
            cluster = c[i]
            if X[i] < minmax[cluster][0]:
                minmax[cluster][0] = X[i]
            if X[i] > minmax[cluster][1]:
                minmax[cluster][1] = X[i]
        
        points_set = sorted(minmax, key =lambda x: (x[0],x[1]))
        level_1 = points_set[0]
        level_2 = points_set[1]
        level_3 = points_set[2]
        level_4 = points_set[3]
        
    
   
    df.at[df.iloc[index]['Datetime'], 'level_1'] = level_1
    df.at[df.iloc[index]['Datetime'], 'level_2'] = level_2
    df.at[df.iloc[index]['Datetime'], 'level_3'] = level_3
    df.at[df.iloc[index]['Datetime'], 'level_4'] = level_4
    
for i in range(110, len(df)):
    plt.scatter(i,df.iloc[i]['Close'], c='b')
    plt.scatter(i,df.iloc[i]['level_1'][0], c='g')
    plt.scatter(i,df.iloc[i]['level_1'][1], c='g')
    plt.scatter(i,df.iloc[i]['level_2'][0], c='r')
    plt.scatter(i,df.iloc[i]['level_2'][1], c='r')
    plt.scatter(i,df.iloc[i]['level_3'][0], c='c')
    plt.scatter(i,df.iloc[i]['level_3'][1], c='c')
    plt.scatter(i,df.iloc[i]['level_4'][0], c='m')
    plt.scatter(i,df.iloc[i]['level_4'][1], c='m')





