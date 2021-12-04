# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:58:46 2021

@author: Spongetheone
"""


with open(r'''day2.txt''') as f:
    lines = f.readlines()

horizontal =0
depth = 0
aim = 0

for i in lines:
    number = int(i.split(" ")[1])

    if "forward" in i:
        horizontal += number
    elif "down" in i:
        depth += number
    elif "up" in i:
        depth -= number
    else:
        print(i)

print("Part 1: ", horizontal*depth)


horizontal =0
depth = 0
aim = 0

for i in lines:
    number = int(i.split(" ")[1])

    if "forward" in i:
        horizontal += number
        depth += number*aim
    elif "down" in i:
        aim += number
    elif "up" in i:
        aim -= number
    else:
        print(i)

print("Part 2:",horizontal*depth)