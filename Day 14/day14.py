# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:52:20 2021

@author: Paddy
"""

with open("day14.txt","r") as f:
    lines = f.read().split('\n')
    
#this is the start polymer
workingString = lines.pop(0)
#one empty line be gone
lines.pop(0)

#dicts are love
polydict = {}
couplecount = {}
lettercounter = {}

#split the working orders into a dict
for i in lines:
    polydict[i.split(" ")[0]] = i.split(" ")[2]

#fillt he dict for counting the letter
for i in range(len(workingString)):
    try:
        lettercounter[workingString[i]] += 1
    except:
        lettercounter[workingString[i]] = 1

#fill the dicts for counting the pairs
for i in range(len(workingString)-1):
    try:
        couplecount[workingString[i]+workingString[i+1]] += 1
    except:
        couplecount[workingString[i]+workingString[i+1]] = 1
    
steps=40
#idea is pretty straifght forward
#Lets say you have NN and put B inside. This becomes NBN. In the next step
#you have to check NB and BN. So instead of creating the string we just count
#the pairs and count the letters
#Its lantern fish all over again
for i in range(steps):
    tempdict = {}
    #couplecount is dict that holds pairs and how often they exist
    for key in couplecount:
        #creat the two pairs
        string1 = key[0]+polydict[key]
        string2 = polydict[key]+key[1]
        #with dicts you always have to try to see if the element is allready in there
        #This dict counts the letters
        try:
            lettercounter[string1[1]] += couplecount[key]
        except:
            lettercounter[string1[1]] = 1
        #this dict holds the pairs and couls
        #since we need to calculate the entire step we cant modify
        #the dict while caluclating the steps. (i think)
        #so lets save it in temp dict and then copy it over
        try:
            tempdict[string1] += couplecount[key]
        except:
            tempdict[string1] = couplecount[key]
        try:
            tempdict[string2] += couplecount[key]
        except:
            tempdict[string2] = couplecount[key]
    couplecount = dict(tempdict)
    
print("Solution for",steps,"steps",lettercounter[max(lettercounter,key=lettercounter.get)] -
      lettercounter[min(lettercounter,key=lettercounter.get)])

