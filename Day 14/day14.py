# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:52:20 2021

@author: Paddy
"""

with open("day14.txt","r") as f:
    lines = f.read().split('\n')
    
workingString = lines.pop(0)
lines.pop(0)

polydict = {}
couplecount = {}
lettercounter = {}

for i in lines:
    polydict[i.split(" ")[0]] = i.split(" ")[2]


for i in range(len(workingString)):
    try:
        lettercounter[workingString[i]] += 1
    except:
        lettercounter[workingString[i]] = 1
        
for i in range(len(workingString)-1):
    try:
        couplecount[workingString[i]+workingString[i+1]] += 1
    except:
        couplecount[workingString[i]+workingString[i+1]] = 1
    


for i in range(40):
    tempdict = {}
    for key in couplecount:
        string1 = key[0]+polydict[key]
        string2 = polydict[key]+key[1]
        #print("Key:",key,"String1",string1,"String2",string2,"Letter",string1[1])
        try:
            lettercounter[string1[1]] += couplecount[key]
        except:
            lettercounter[string1[1]] = 1
        try:
            tempdict[string1] += couplecount[key]
        except:
            tempdict[string1] = couplecount[key]
        try:
            tempdict[string2] += couplecount[key]
        except:
            tempdict[string2] = couplecount[key]
    couplecount = dict(tempdict)
    #print(lettercounter)
    
print("Solution for",40,"steps",lettercounter[max(lettercounter,key=lettercounter.get)] -
      lettercounter[min(lettercounter,key=lettercounter.get)])

