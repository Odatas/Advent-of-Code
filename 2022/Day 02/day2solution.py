# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:14:08 2022

@author: patri
"""

with open(r'''input.txt''') as f:
    puzzel_input = f.readlines()
puzzel_input = [x.strip() for x in puzzel_input]   

#A,X Rock (1), B,Y Paper (2), C,Z Scissors (3)
#Loss (0), Draw (3), Win (6)
point_dict = {
    "A X":4,
    "A Y":8,
    "A Z":3,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":7,
    "C Y":2,
    "C Z":6
    }

points_after_all_rounds = 0
for i in puzzel_input:
    points_after_all_rounds += point_dict[i]
    
print("Part 1:",points_after_all_rounds)

#A Rock (1), B Paper (2), C Scissors (3)
#X Loss (0), Y Draw (3), Z Win (6)
point_dict_part2 = {
    "A X":3,
    "A Y":4,
    "A Z":8,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":2,
    "C Y":6,
    "C Z":7
    }

points_after_all_rounds = 0
for i in puzzel_input:
    points_after_all_rounds += point_dict_part2[i]
    
print("Part 2:",points_after_all_rounds)