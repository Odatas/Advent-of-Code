# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 22:46:48 2021

@author: Paddy
"""

import copy

with open("day25.txt","r") as f:
    lines = f.read().split('\n')
    
lines = [list(x) for x in lines]

counter = 0
changed = True
while changed:
    counter +=1
    print(counter)

    tempField = copy.deepcopy(lines)
    beforeField = copy.deepcopy(lines)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j == len(lines[i])-1:
                if tempField[i][0] == "." and tempField[i][j] == ">":
                    lines[i][0] = ">" 
                    lines[i][j] = "."
            else:
                if tempField[i][j] == ">" and tempField[i][j+1] == ".":
                    lines[i][j] = "." 
                    lines[i][j+1] = ">"
                    j+=1
    
    tempField = copy.deepcopy(lines)
    
    #j ist zeilennummer
    for j in range(len(lines[0])):
        #i ist spaltennummer
        for i in range(len(lines)):
            if i == len(lines)-1:
                if tempField[0][j] == "." and tempField[i][j] == "v":
                    lines[i][j] = "."
                    lines[0][j] = "v"
            else:
                if tempField[i+1][j] == "." and tempField[i][j] == "v":
                    lines[i+1][j] = "v"
                    lines[i][j] = "."
                    i+=1
    for i in range(len(lines)):
        if lines[i] == beforeField[i]:
            changed = False
            pass
        else:
            changed = True
            break
    
