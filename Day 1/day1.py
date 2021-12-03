# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:22:16 2021

@author: pphilipiak
"""

with open(r'''C:\Users\pphilipiak\Documents\Advent of Code\Day 1\day1.txt''') as f:
    lines = f.readlines()

numbers=[]
for i in lines:
    numbers.append(int(i))

lastnumber=numbers[0]
counter=0
for number in numbers:
    if number > lastnumber:
        counter +=1
    lastnumber=number

print("Part 1: ",counter)

lastWindow=numbers[0]+numbers[1]+numbers[2]
counter=0
for i in range(len(numbers)-2):
    windowA = numbers[i]+numbers[i+1]+numbers[i+2]
    if windowA > lastWindow:
        counter +=1
    lastWindow = numbers[i]+numbers[i+1]+numbers[i+2]

print("Part 2: ",counter)