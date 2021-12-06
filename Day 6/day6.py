# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 06:44:39 2021

@author: Spongetheone
"""

lanternFish=[0]
with open(r'''day6.txt''') as f:
    lanternFishPopulation = [[int(x) for x in line.split(",")] for line in f][0]


days = 256

for i in range(days):
    print("Day:", i,"Number of Fish:",len(lanternFishPopulation))
    for index in range(len(lanternFishPopulation)):
        lanternFishPopulation[index] -=1
        if lanternFishPopulation[index] < 0:
            lanternFishPopulation[index] = 6
            lanternFishPopulation.append(8)

print("Part1:",len(lanternFishPopulation))
