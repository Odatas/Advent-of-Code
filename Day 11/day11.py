# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 07:59:22 2021

@author: Spongetheone
"""

import numpy as np

def Flash(iy,ix):
    flashCounter = 1
    #check all adjecent fields
    for k in stepsVariations:
        if iy+k[0] in range(0,Matrix.shape[0]) and ix+k[1] in range(0,Matrix.shape[1]):
            if flashDetector[iy+k[0]][ix+k[1]] == 0:
                Matrix[iy+k[0]][ix+k[1]] +=1
                if Matrix[iy+k[0]][ix+k[1]] > 9:
                    Matrix[iy+k[0]][ix+k[1]] = 0
                    flashDetector[iy+k[0]][ix+k[1]] = 1
                    flashCounter+=Flash(iy+k[0],ix+k[1])
    return flashCounter


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
for i in range(-1,2):
    for j in range (-1,2):
        stepsVariations.append((i,j))
stepsVariations.remove((0,0))

while True:
    steps+=1
    flashDetector = np.zeros(Matrix.shape)
    Matrix +=1
    for iy,ix in np.ndindex(Matrix.shape):
        if Matrix[iy][ix] > 9:
            Matrix[iy][ix] = 0
            flashDetector[iy][ix] = 1
            flashCounter+=Flash(iy,ix)
    if steps == 100:
        print("Part 1:", flashCounter)
    if np.all(Matrix == Matrix[0]):
        print("Part 2:",steps)
        break


