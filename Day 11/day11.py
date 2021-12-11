# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 07:59:22 2021

@author: Spongetheone
"""

import numpy as np

#Increases for a Field in the Matrix all Charges by 1 and checks if they Flash themself.
def Flash(iy,ix):
    flashCounter = 1
    Matrix[iy][ix] = 0
    flashDetector[iy][ix] = 1
    for k in stepsVariations:
        if iy+k[0] in range(0,Matrix.shape[0]) and ix+k[1] in range(0,Matrix.shape[1]):
            if flashDetector[iy+k[0]][ix+k[1]] == 0:
                Matrix[iy+k[0]][ix+k[1]] +=1
                if Matrix[iy+k[0]][ix+k[1]] > 9:
                    Matrix[iy+k[0]][ix+k[1]] = 0
                    flashDetector[iy+k[0]][ix+k[1]] = 1
                    flashCounter+=Flash(iy+k[0],ix+k[1])
    return flashCounter

#there is probably a smater way to do this. Someone help me.
with open("day11.txt","r") as f:
    lines = f.readlines()
matrixInput=[]
for i in lines:
    line = [int(x) for x in i.strip()]
    matrixInput.append(line)
Matrix = np.stack(matrixInput)


steps=0
flashCounter=0
stepsVariations = []
flashDetecter = []
#creat list of steps to check
for i in range(-1,2):
    for j in range (-1,2):
        stepsVariations.append((i,j))
stepsVariations.remove((0,0))

#Lets go flashing
while True:
    steps+=1
    #creat a Matrix to see if a field allready flashed
    flashDetector = np.zeros(Matrix.shape)
    #All fields in matrix +1, yes its that easy with numpy
    Matrix +=1
    #lets go through all the fields
    for iy,ix in np.ndindex(Matrix.shape):
        #some charge bigger 9 detected
        if Matrix[iy][ix] > 9:
            #Lets flash baby 
            flashCounter+=Flash(iy,ix)
    #Part 1 check after 100 steps how many flashes
    if steps == 100:
        print("Part 1:", flashCounter)
    #Part two check when all are syncronized. Yes its that easy with numpy
    if np.all(Matrix == Matrix[0]):
        print("Part 2:",steps)
        #should probably stop here. Question remains why are octopuses
        #not synchen in the first place when entering cave
        #Someone must have reste them
        #Im not alone.
        break


