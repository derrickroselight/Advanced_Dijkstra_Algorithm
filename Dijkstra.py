import numpy as np
import pandas as pd

df = pd.read_csv('/Users/Light/PythonData/dijkstra.txt', sep=" ", dtype=object,header=None, names=["start", "end", "dis", "width" ,"bool"],engine='python')
df['Road'] = df.index

# Set up distance and width matrices 
# inf = infinity
# d = distance, w = width, r = road
d = np.zeros((int(df.iloc[0][0]), int(df.iloc[0][0])), dtype=int)
w = np.zeros((int(df.iloc[0][0]), int(df.iloc[0][0])), dtype=int)
r = np.zeros((int(df.iloc[0][0]), int(df.iloc[0][0])), dtype=int)
inf = 99999999
tsp = {1:'Walk', 2:'Bike', 3:'Scooter', 4:'Car', 5:'Bus'}
width = {1:0.5, 2:1.5, 3:2, 4:4, 5:6}

# n : number of nodes 
# m : number of roads
# 
n = int(df.iloc[0][0])
m = len(df.index) - 1

# initializion
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
            
# Input distance, width, and road data into respective matrices
for i in range(1, m+1):
    d[int(df.iloc[i][0])][int(df.iloc[i][1])] = int(df.iloc[i][2])
    w[int(df.iloc[i][0])][int(df.iloc[i][1])] = int(df.iloc[i][3])
    r[int(df.iloc[i][0])][int(df.iloc[i][1])] = int(df.iloc[i][5])
  
# Choose start node, end node, and transportation  
start, end, method = map(int, input().split(' '))
    
    
# initial distance array to record the beginning status
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

# initial "sure" array
sure = np.zeros(int(df.iloc[0][0]), dtype=int)
sure[start] = 1

# Dijkstra Algorithm
for i in range(0, n-1):
    # Find the nearest node to start node
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

# Output
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
