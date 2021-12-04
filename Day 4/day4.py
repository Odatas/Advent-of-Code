# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 07:43:22 2021

@author: Odatas
"""

import numpy

def testForBingo(matrix):
    a = numpy.sum(matrix,axis=0)  
    b = numpy.sum(matrix,axis=1)  
    for i in a:
        if i > 4:
            return True
    for i in b:
        if i > 4:
            return True
    return False

def calculateSum(matrix,shadow):
    matrixsum=0
    for i in range(5):
        for j in range(5):
            if shadow[i][j]==0:
                matrixsum += matrix[i][j]
                
    return matrixsum


with open('day4.txt') as f:
    first_line = f.readline()
    draws = [int(s) for s in first_line.split(",")]
    
data = numpy.loadtxt('day4.txt',skiprows=2)
bingoCards = numpy.array_split(data,len(data)/5)



shadow = []

for i in range(int(len(data)/5)):
    shadow.append(numpy.zeros((5,5)))
    
test = []
bingo=False
tupelList=[]
for bingoDraw in draws:
    for cardNumber in range(len(bingoCards)):
        if bingoDraw in bingoCards[cardNumber] :
            if len([item for item in tupelList if item[0] == cardNumber]) > 0:
                continue
            tupel=numpy.where(bingoDraw == bingoCards[cardNumber])
            shadow[cardNumber][tupel[0][0]][tupel[1][0]] = 1
            if testForBingo(shadow[cardNumber]):
                if len([item for item in tupelList if item[0] == cardNumber]) == 0:
                    tupelList.append((cardNumber,bingoDraw))
                
print(tupelList)
first = (0,0)
last = (0,0)
for bingoDraw in draws:
    for tupel in tupelList:
        if bingoDraw == tupel[1]:
            last = tupel
            if first == (0,0):
                first = tupel
                
print("Part 1:", first[1] * calculateSum(bingoCards[first[0]],shadow[first[0]]))
print("Part 2:", last[1] * calculateSum(bingoCards[last[0]],shadow[last[0]]))



