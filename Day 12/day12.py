# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 09:29:14 2021

@author: Paddy
"""

import networkx as nx 

def hasNoSmallDouble(liste):
    for i in liste:
        if i.islower() and liste.count(i) > 1:
            return False
    return True

def findNextNodeToString(way):
    neighbors =G.adj[way[-1]]

    for i in neighbors:
        if i == "start":
            continue
        if i == "end":
            temp2 = [x for x in way]
            temp2.append(i)
            paths.append(temp2)
            #print("Found:",temp2)
            continue
        if i.islower():
            if way.count(i) < 1 or (way.count(i) < 2 and hasNoSmallDouble(way)):
                #print("Pass:",i,way)
                pass
            else:
                #print("Blocked:",i,way)
                continue
        tempList = [x for x in way]
        tempList.append(i)
        findNextNodeToString(tempList)
        
with open("day12.txt","r") as f:
    lines = f.read().split('\n')
    
graph = [x.split("-") for x in lines ]

G=nx.Graph()
G.add_edges_from(graph)
nx.draw(G,with_labels = True)

paths=[]
way = ["start"]
findNextNodeToString(way)
print("Part1:",len(paths))