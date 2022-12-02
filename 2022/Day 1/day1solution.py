# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:41:41 2022

@author: patri
"""

with open(r'''C:\Users\patri\Documents\GitHub\Advent-of-Code\2022\Day 1\input.txt''',"r") as f:
    puzzel_input = f.read()
    
puzzel_input = puzzel_input.split("\n\n")

def calorieCounter(calorie_string):
    calorie_list = calorie_string.split("\n")
    calorie_sum = 0
    for i in calorie_list:
        if i != "":
            calorie_sum += int(i)
        
    return calorie_sum
calorie_list = []
for i in puzzel_input:
    calorie_list.append(calorieCounter(i))

calorie_list.sort()
print("Part 1",calorie_list[-1])
print("Part 2",sum(calorie_list[-3:]))        
        
    
    
