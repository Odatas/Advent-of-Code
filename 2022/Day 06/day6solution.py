# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 06:35:03 2022

@author: patri
"""
from collections import Counter


with open("input.txt", "r") as f:
    puzzel_input = f.read()

part1 = False
part2 = False
for i in range(len(puzzel_input)-3):
    if len(Counter(puzzel_input[i:i+4])) >= 4 and not part1:
        print("Part 1:", i+4)
        part1 = True
    if len(Counter(puzzel_input[i:i+14])) >= 14 and not part2:
        print("Part 2:", i+14)
        part2 = True
    if part1 and part2:
        break
