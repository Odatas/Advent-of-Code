# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:24:52 2022

@author: patri
"""
import re

with open("input.txt", "r") as f:
    puzzel_input = f.readlines()


containment = 0
full_containment = 0
for i in puzzel_input:
    numbers = re.findall(r'\d+', i)
    numbers = [int(x) for x in numbers]
    
    if numbers[0] <= numbers[2] and numbers[1] >= numbers[3]:
        containment += 1
    elif numbers[2] <= numbers[0] and numbers[3] >= numbers[1]:
        containment += 1
        
    if numbers[0] <= numbers[2] and numbers[1] >= numbers[2]:
        full_containment += 1
        print("First",i)
    elif numbers[2] <= numbers[0] and numbers[3] >= numbers[0]:
        full_containment += 1
        print("Second",i)

print("Part 1:",containment)
print("Part 2:",full_containment)