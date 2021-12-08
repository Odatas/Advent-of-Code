# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:37:30 2021

@author: Spongetheone
"""

with open("day7.txt") as f:
    lines = f.readlines()

counterOne = 0
counterFour = 0
counterSeven = 0
counterEight = 0

for i in lines:
    for j in i.split(" | ")[1].split(" "):
        if len(j) == 2:
            counterOne += 1
        if len(j) == 3:
            counterSeven += 1
        if len(j) == 4:
            counterFour += 1
        if len(j) == 7:
            counterEight += 1

print ("Part 1: ", counterOne+counterSeven+counterFour+counterEight)