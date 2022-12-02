# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:45:47 2021

@author: Spongetheone
"""
import numpy as np


with open("day13.txt","r") as f:
    lines = f.read().split('\n')

constructor = []
instructions = []
for i in lines:
    if i == "":
        continue
    if "fold" in i:
        instructions.append(i)
    else:
        constructor.append( (int(i.split(",")[0]) , int(i.split(",")[1])) )

constructorMatrix = np.stack(constructor)

#turns out the size of the matrix is not determined by the highes value x and y wise
#but by the line in which to fold. 
#matrix = np.zeros((np.amax(constructorMatrix[:,1])+1,np.amax(constructorMatrix[:,0])+1))
matrix = np.zeros((895,1311))

print(matrix)
for i in constructorMatrix:
    matrix[i[1]][i[0]] = 1
    
for i in instructions:
    print(i)
    if "x" in i:
        x =  int(i.split(" ")[2].split("=")[1])
        a = matrix[:,:x]
        b = matrix[:,x+1:]
        matrix = a+np.flip(b, axis=1)
        
    if "y" in i:
        y =  int(i.split(" ")[2].split("=")[1])
        a = matrix[:y,]
        b = matrix[y+1:,]
        matrix = a+np.flip(b, axis=0)
    print("Matrix shape",matrix.shape)
    print("Zeros:",np.count_nonzero(matrix))
    

