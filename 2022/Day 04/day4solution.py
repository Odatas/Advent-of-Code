# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:24:52 2022

@author: patri
"""
import re

with open("input.txt", "r") as f:
    puzzel_input = f.readlines()


partial_containment = 0
full_containment = 0
for i in puzzel_input:
    numbers = re.findall(r'\d+', i)
    numbers = [int(x) for x in numbers]

    if numbers[0] <= numbers[2] and numbers[1] >= numbers[3]:
        full_containment += 1
    elif numbers[2] <= numbers[0] and numbers[3] >= numbers[1]:
        full_containment += 1

    if numbers[0] <= numbers[2] and numbers[1] >= numbers[2]:
        partial_containment += 1
    elif numbers[2] <= numbers[0] and numbers[3] >= numbers[0]:
        partial_containment += 1

print("Part 1:", full_containment)
print("Part 2:", partial_containment)
