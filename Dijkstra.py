#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:32:52 2019

@author: Light
"""
import numpy as np
import pandas as pd
#讀入資料

df = pd.read_csv('/Users/Light/PythonData/dijkstra2.txt', sep=" ", dtype=object,header=None, names=["start", "end", "dis", "width" ,"bool"],engine='python')
df['Route'] = df.index

# 建立距離與寬度矩陣
# inf = infinity
# d = distance, w = width, r = route
d = np.zeros((int(df.iloc[0][0]), int(df.iloc[0][0])), dtype=int)
w = np.zeros((int(df.iloc[0][0]), int(df.iloc[0][0])), dtype=int)
r = np.zeros((int(df.iloc[0][0]), int(df.iloc[0][0])), dtype=int)
inf = 99999999
tsp = {1:'Walk', 2:'Bike', 3:'Scooter', 4:'Car', 5:'Bus'}
width = {1:0.5, 2:1.5, 3:2, 4:4, 5:6}
#讀入起點 終點 交通工具
start, end, method = map(int, input().split(' '))

# n個點 m個邊
n = int(df.iloc[0][0])
m = len(df.index) - 1

# 初始化
for i in range(0, n):
    for j in range(0, n):
        if i == j : 
            d[i][j] = 0
        else:
            d[i][j] = inf
            
for i in range(0, n):
    for j in range(0, n):
        if i == j : 
            w[i][j] = 0
        else:
            w[i][j] = inf   

for i in range(0, n):
    for j in range(0, n):
        if i == j : 
            r[i][j] = 0
        else:
            r[i][j] = inf               
            
# 輸入距離資料與路幅資料與路名
for i in range(1, m+1):
    d[int(df.iloc[i][0])][int(df.iloc[i][1])] = int(df.iloc[i][2])
    w[int(df.iloc[i][0])][int(df.iloc[i][1])] = int(df.iloc[i][3])
    r[int(df.iloc[i][0])][int(df.iloc[i][1])] = int(df.iloc[i][5])
    
# 初始距離陣列，從起點到其餘各點的初始路程
record = [[],[],[],[],[],[],[]]
dis = np.zeros(int(df.iloc[0][0]), dtype=int)
for i in range(0, n):
    if w[start][i] >= width[method]:
        dis[i] = d[start][i]
        record[i].append(r[start][i])
    else:
        dis[i] = inf
       
for i in range(0, n):
    print(dis[i])        

# 初始 book 陣列
sure = np.zeros(int(df.iloc[0][0]), dtype=int)
sure[start] = 1

# Dijkstra Algorithm
for i in range(0, n-1):
    # 找到離 start 點最近的頂點
    min = inf
    for j in range(0, n):
        if (sure[j] == 0) and (dis[j] < min) and (w[start][j] >= width[method]):
            min = dis[j]
            u = j
    sure[u] = 1
        
    for v in range(0, n):
        if d[u][v] < inf:
            if (dis[v] > dis[u] + d[u][v]) and (w[u][v] >= width[method]):
                dis[v] = dis[u] + d[u][v]
                if sure[u] == 1 :
                      record[v].clear()
                for k in range(len(record[u])):      
                      record[v].append(record[u][k])
                record[v].append(r[u][v])

# 輸出
for i in range(0, n):
    print(dis[i])

print('Start Point : %d' %start)
print('Destination : %d' %end)
print('Transportation : %s' %tsp[method])
print('Width Needed : %s' %width[method])
print('Total Distance : %d' %dis[end])
print('Route & Width:')
if record[end] == [inf]: print('Can not reach the end')
elif record[end] == []: print('start = end')
else:
    for i in range(len(record[end])):
        print("%d -> %d Distance : %d Width : %d Limits : %s" %(int(df.iloc[record[end][i]][0]),int(df.iloc[record[end][i]][1]),int(df.iloc[record[end][i]][2]),int(df.iloc[record[end][i]][3]),df.iloc[record[end][i]][4]) )






