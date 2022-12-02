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

#Rekursion again because it goes brr
def findNextNodeToString(way,withExtra = False):
    #start with a list of nodes. The last one is the current node
    neighbors =G.adj[way[-1]]
    #go through all neighbors
    for i in neighbors:
        #If a neighbor is start. Skipp him
        if i == "start":
            continue
        #if a neighbor is end we found a path so save him for late
        if i == "end":
            temp2 = [x for x in way]
            temp2.append(i)
            paths.append(temp2)
            #print("Found:",temp2)
            continue
        #if the neighber is lowercase special rules aplly
        if i.islower():
            #2 modes: Allow 1 double visit of lowercase and allow no double visits
            if withExtra:
                if way.count(i) < 1 or (way.count(i) < 2 and hasNoSmallDouble(way)):
                    pass
                else:
                    continue
            else:
                if way.count(i) > 0:
                    continue
        # when lowercase rule is ok append node to list and call function again
        tempList = [x for x in way]
        tempList.append(i)
        findNextNodeToString(tempList,withExtra)

with open("day12.txt","r") as f:
    lines = f.read().split('\n')
#Get list of edges (those are the connections from one node to another)
graph = [x.split("-") for x in lines ]
#create graph
G=nx.Graph()
#fill graph withs edges. Yes its that easy. Python amazing.
G.add_edges_from(graph)
#draw graph just for the luls.
nx.draw(G,with_labels = True)

#creat list for all possible paths.
paths=[]
#add start to it
way = ["start"]
#Recursion goes brrr
findNextNodeToString(way,withExtra = False)
#success
print("Part 1:",len(paths))
#do it again with weird extra rule
paths=[]
findNextNodeToString(way,withExtra = True)
#great success
print("Part 2:",len(paths))

#submarine has great capabilitys maping all of the caves from the start position
#That brings up question: who send me on this  mission?
#My Memory is gone. I cant remeber anything before i was dropped in water
#Yes functionallity of sub comes easy to me
#Maybe i am spy? I have to be carefull who i talk to