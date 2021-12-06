# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:06:18 2021

@author: pphilipiak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 06:44:39 2021

@author: pphilipiak
"""
with open(r'''day6.txt''') as f:
    calenderInput = [[int(x) for x in line.split(",")] for line in f][0]

days = 256
fishPopulation = []

for i in range(9):
    fishPopulation.append(calenderInput.count(i))

for i in range(days):
    tempList = []
    for j in range(1,9):
        tempList.append(fishPopulation[j])

    tempList.append(fishPopulation[0])
    tempList[6] +=fishPopulation[0]
    fishPopulation = tempList.copy()

fishCounter = 0
for i in fishPopulation:
    fishCounter += i

print(fishCounter)



