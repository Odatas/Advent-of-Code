# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 06:42:46 2021

@author: Spongetheone
"""

import numpy as np

with open(r'''day7.txt''') as f:
    calenderInput = [[int(x) for x in line.split(",")] for line in f][0]
    
    

matrixInput  = []
matrixInput2 = []
matrixSize = max(calenderInput)
for i in calenderInput:
    entry  = np.zeros(matrixSize+1)
    entry2 = np.zeros(matrixSize+1)
    for j in range(1,matrixSize+1):
        if(i-j) < 0:
            pass
        else:
            entry[i-j] = j
            entry2[i-j] = j + entry2[i-j+1]
        if(i+j>matrixSize):
           pass
        else:
            entry[i+j] = j
            entry2[i+j] = j + entry2[i+j-1]
    matrixInput.append(entry)
    matrixInput2.append(entry2)
costMatrix = np.stack(matrixInput)
costMatrix2 = np.stack(matrixInput2)

print("Part1:",costMatrix.sum(axis=0).min())
print("Part2:",costMatrix2.sum(axis=0).min())
