# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 07:43:22 2021

@author: Odatas
"""

import numpy

#Checks a matrix for bingo
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

#calculate the sum of the filds of the matrix which are 0 on the shadow
def calculateSum(matrix,shadow):
    matrixsum=0
    for i in range(5):
        for j in range(5):
            if shadow[i][j]==0:
                matrixsum += matrix[i][j]
                
    return matrixsum

#get the bingo number draw
with open('day4.txt') as f:
    first_line = f.readline()
    draws = [int(s) for s in first_line.split(",")]

#get the bingo cards
data = numpy.loadtxt('day4.txt',skiprows=2)
bingoCards = numpy.array_split(data,len(data)/5)
#Creat the shadow for marking nubmers on bingocard
shadow = []
for i in range(int(len(data)/5)):
    shadow.append(numpy.zeros((5,5)))

#Tupel List for Cardnumber and which number made the Card win bingo
tupelList=[]
#Go throu all draws
for bingoDraw in draws:
    #check every card
    for cardNumber in range(len(bingoCards)):
        #if the drawn number is in the bingo card check it
        if bingoDraw in bingoCards[cardNumber] :
            #if the bingocard allready won, skip it
            if len([item for item in tupelList if item[0] == cardNumber]) > 0:
                continue
            #look up the field where the number is
            tupel=numpy.where(bingoDraw == bingoCards[cardNumber])
            #mark the field in the shadowcard
            shadow[cardNumber][tupel[0][0]][tupel[1][0]] = 1
            #check if the card has now a Bingo
            if testForBingo(shadow[cardNumber]):
                #when bingo save card and number which made card win
                if len([item for item in tupelList if item[0] == cardNumber]) == 0:
                    tupelList.append((cardNumber,bingoDraw))
first = (0,0)
last = (0,0)
#go through all draws again and save the first occuring winner and the last one
for bingoDraw in draws:
    for tupel in tupelList:
        if bingoDraw == tupel[1]:
            last = tupel
            if first == (0,0):
                first = tupel
                
print("Part 1:", first[1] * calculateSum(bingoCards[first[0]],shadow[first[0]]))
print("Part 2:", last[1] * calculateSum(bingoCards[last[0]],shadow[last[0]]))



