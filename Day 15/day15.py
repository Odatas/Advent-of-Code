# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:37:05 2021

@author: Paddy
"""
import numpy as np
import networkx as nx
import copy
import matplotlib.pyplot as plt

with open("day15example.txt","r") as f:
    lines = f.readlines()
matrixInput=[]
for i in lines:
    line = [int(x) for x in i.strip()]
    matrixInput.append(line)
temp=copy.deepcopy(matrixInput)
for iy in range(len(temp)):
    for runde in range(1,5):
        for ix in temp[iy]:
            newnumber=ix+runde
            if newnumber >9:
                newnumber-=9
            matrixInput[iy].append(newnumber)
temp = copy.deepcopy(matrixInput)
for runde in range(1,5):
    for iy in range(len(temp)):
        temprow=[]
        for ix in temp[iy]:
            newnumber=ix+runde
            if newnumber > 9:
                newnumber -= 9
            temprow.append(newnumber)
        matrixInput.append(temprow)



A = np.stack(matrixInput)

stepsVariations = []
stepsVariations.append((0,1))
stepsVariations.append((0,-1))
stepsVariations.append((-1,0))
stepsVariations.append((1,0))

G=nx.DiGraph()
for iy,ix in np.ndindex(A.shape):
    for k in stepsVariations:
        if iy+k[0] in range(0,A.shape[0]) and ix+k[1] in range(0,A.shape[1]):
            G.add_edge(str(iy)+"," +str(ix), str(iy+k[0])+"," +str(ix+k[1]), weight=A[iy+k[0]][ix+k[1]])




print(nx.dijkstra_path_length(G,"0,0",str(A.shape[0]-1)+ "," + str(A.shape[1]-1)))
pathNodeList = nx.dijkstra_path(G,"0,0",str(A.shape[0]-1)+ "," + str(A.shape[1]-1))
p = nx.shortest_path(G,"0,0",str(A.shape[0]-1)+ "," + str(A.shape[1]-1))
for e in G.edges():
    G[e[0]][e[1]]['color'] = 'black'
for i in range(len(p)-1):
    G[p[i]][p[i+1]]['color'] = 'red'
edge_color_list = [ G[e[0]][e[1]]['color'] for e in G.edges() ]
nx.draw(G, node_size=3,arrowsize=1,width=0.3,with_labels=True,font_size=2,edge_color = edge_color_list)
plt.savefig('plot4.png', dpi=1000, bbox_inches='tight')
plt.show()
print("Done")