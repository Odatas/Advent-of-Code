# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 06:53:47 2022

@author: patri
"""
import re


def Move_Stack_by_Column(home, destination, ammount=1):
    crate = ""
    for i in range(len(stackmatrix)):
        if stackmatrix[i][home] != " ":
            crate += stackmatrix[i][home]
            stackmatrix[i][home] = " "
            ammount -= 1
            if ammount == 0:
                break
    for singlecrate in reversed(crate):
        for i in reversed(range(len(stackmatrix))):
            if stackmatrix[i][destination] == " ":
                stackmatrix[i][destination] = singlecrate
                break


def createMatrix():
    stackmatrix = []
    for i in range(rowrange*rowrange):
        row = []
        for j in range(rowrange):
            row.append(" ")
        stackmatrix.append(row)

    for i in range(rows):
        row = []
        for j in range(rowrange):
            row.append(puzzel_input[i][4*j+1])
        stackmatrix.append(row)
    return stackmatrix


def getTopCrates():
    topcrates = ""
    for i in range(rowrange):
        for j in range(len(stackmatrix)):
            if stackmatrix[j][i] != " ":
                topcrates += stackmatrix[j][i]
                break
    return topcrates


with open("input.txt", "r") as f:
    puzzel_input = f.readlines()

rowrange = 9
rows = 8


stackmatrix = createMatrix()
for i in puzzel_input:
    if i[0] == "m":
        ammount, start, end = re.findall(r'\d+', i)
        for i in range(int(ammount)):
            Move_Stack_by_Column(int(start)-1, int(end)-1)


print("Part1: ", getTopCrates())

stackmatrix = createMatrix()
for i in puzzel_input:
    if i[0] == "m":
        ammount, start, end = re.findall(r'\d+', i)
        Move_Stack_by_Column(int(start)-1, int(end)-1, int(ammount))


print("Part 2:", getTopCrates())
