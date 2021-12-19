# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:38:11 2021

@author: Paddy
"""
import numpy as np
import math
from scipy.spatial.transform import Rotation as R

#checks for two lists the ammount of vecters which are in both lists
#someone can probably do it smarter
def checkPointCounter(U,V,ankerCorrecter):
    counter = 0
    solution=[]
    for i in U:
        for j in V:
            if i[0]==round(j[0]) and i[1]==round(j[1]) and i[2]==round(j[2]):
                #print("Match",i,j)
                solution.append(i+ankerCorrecter)
                counter+=1
    if counter > 11:
        global listofbeacons
        listofbeacons+=solution
    #since we build the anchor from the point, we should always have at least 1 matching point.
    if counter == 0:
        print("Shit")
    return counter

#meet of the game. The idea is simple. Get the difference between 2 points. This shall be the annchor.
#Try with the anchor all points and see if 12 points match the points from the other scanners viewpoint.
def findScanner(scannerValues,originPoints,ankerCorrecter):
    #entry is the list of scanpoints from the scanner POV
    for entry in scannerValues:
        for i in entry:
            #if entry and originaPoints are equal, skipp test because we would find [0,0,0] as suitable 
            if np.array_equal(originPoints,entry):
                break
            for j in originPoints:
                #orientation of the scanner might be different so we just try every possible rotation
                for degree in radiants:
                    for axis in orientations:
                        #rotatet vector
                        rotatetvector = R.from_euler(axis, degree, degrees=True).apply(i)
                        #calculate difference, this is the Anchor
                        Anker = j-rotatetvector #np.subtract(j,rotatetvector)
                        #Move all the Points and also rotate them.
                        tempPoints=Anker+R.from_euler(axis, degree, degrees=True).apply(entry)
                        #check how much matches we have
                        if checkPointCounter(originPoints,tempPoints,ankerCorrecter) > 11:
                            #more than 11? Bingo just save this.
                            print(Anker+ankerCorrecter)
                            listofscanner.append(Anker+ankerCorrecter)
                            if len(listofscanner)<len(scannerValues):
                                #print("Found one for",entry)
                                findScanner(scannerValues[1:], entry, Anker)
                            return
#all the radiants
radiants=[-270,-180,-90,0,90,180,270,360]
#all the axis
orientations = ["x","y","z"]

#readin and preparing of data
with open("day19example.txt","r") as f:
    lines = f.read().split('\n')
scannerValues =[]
singleScanner=[]
for i in lines:
    if "--- scanner" in i:
        if len(singleScanner) > 0:
            scannerValues.append(np.stack(singleScanner))
            singleScanner = []
    elif i == "":
        continue
    else:
        singleScanner.append(np.array([int(x) for x in i.split(",")]))
scannerValues.append(np.stack(singleScanner))
listofscanner=[]
#we know 1 scanner allread
listofscanner.append(np.array([0,0,0],"float64"))
listofbeacons = []

#lets do this
findScanner(scannerValues,scannerValues[0].copy(),listofscanner[0])
print("Done")