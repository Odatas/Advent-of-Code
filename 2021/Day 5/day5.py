# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 08:20:56 2021

@author: Paddy
"""

import numpy

def markField(x1,x2,y1,y2):
    #Vertical
    if x1==x2:
        if y2>y1:
            for j in range(y1,y2+1):
                field[j][x1] += 1
            return
        else:
            for j in range(y2,y1+1):
                field[j][x1] += 1
            return
    #Horizontal
    if y1==y2:
        if x2>x1:
            for j in range(x1,x2+1):
                field[y1][j] +=1
            return
        else:
            for j in range(x2,x1+1):
                field[y1][j] +=1
            return
    #Everything else is Diagonal
    i=x1
    j=y1
    while True:
        field[j][i] +=1
        if x1 < x2:
            i += 1
        else:
            i -= 1
        if y1 < y2:
            j += 1
        else:
            j -= 1
        if (i,j) == (x2,y2):
            field[j][i] +=1
            break
        
    
    

with open(r'''day5.txt''') as f:
    lines = f.readlines()
    
size = 1000
field = numpy.zeros((size,size))

for i in lines:
    x1,y1 = i.split(" -> ")[0].split(",")
    x2,y2 = i.split(" -> ")[1].split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    markField(x1,x2,y1,y2)
      
dangerCounter=0

for i in range(size):
    for j in range(size):
        if field[i][j] > 1:
            dangerCounter +=1
print(dangerCounter)
        
