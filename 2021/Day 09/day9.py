# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 06:47:59 2021

@author: pphilipiak
"""
import numpy as np
import sys
print(sys.getrecursionlimit())

def checkBasin(iy,ix,pointsChecked):
    counter = 0
    pointsChecked.append((iy,ix))
    if iy > 0 and  Matrix[iy-1,ix] < 9 and (iy-1,ix) not in pointsChecked:
        counter += checkBasin(iy-1,ix,pointsChecked)

    if iy < Matrix.shape[0]-1 and Matrix[iy+1,ix] <9 and (iy+1,ix) not in pointsChecked:
        counter += checkBasin(iy+1,ix,pointsChecked)

    if ix > 0 and  Matrix[iy,ix-1] < 9 and (iy,ix-1) not in pointsChecked:
        counter += checkBasin(iy,ix-1,pointsChecked)

    if ix < Matrix.shape[1]-1 and Matrix[iy,ix+1] < 9 and (iy,ix+1) not in pointsChecked:
        counter += checkBasin(iy,ix+1,pointsChecked)
    return counter +1

with open("day9.txt","r") as f:
    lines = f.readlines()

matrixInput=[]
basinSize = []
lowPoints = 0

for i in lines:

    line = [int(x) for x in i.strip()]
    matrixInput.append(line)

Matrix = np.stack(matrixInput)

for iy,ix in np.ndindex(Matrix.shape):
    #look up
    if iy > 0 and Matrix[iy,ix] >= Matrix[iy-1,ix]:
        continue

    if iy < Matrix.shape[0]-1 and Matrix[iy,ix] >= Matrix[iy+1,ix] :
        continue

    if ix > 0 and Matrix[iy,ix] >= Matrix[iy,ix-1]:
        continue

    if ix < Matrix.shape[1]-1 and Matrix[iy,ix] >= Matrix[iy,ix+1]:
        continue
    pointsChecked = []
    basinSize.append(checkBasin(iy,ix,pointsChecked))
    lowPoints +=  Matrix[iy,ix]   + 1

print("Part 1:", lowPoints)

basinSize.sort(reverse=True)

print("Part2:",basinSize[0]*basinSize[1]*basinSize[2])


