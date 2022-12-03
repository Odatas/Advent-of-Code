# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:00:04 2022

@author: patri
"""

with open("input.txt", "r") as f:
    puzzel_input = f.readlines()


def Char_Value(character):
    if character.islower():
        return ord(character)-96
    elif character.isupper():
        return ord(character)-38

sum_of_double_items = 0
for i in puzzel_input:
    break_up_point = int(len(i)/2)
    item = set(i[:break_up_point]) & set(i[break_up_point:])
    if item:
        sum_of_double_items += Char_Value(item.pop())

print("Part 1:", sum_of_double_items)

sum_of_badges = 0
for i in range(0, len(puzzel_input)-2, 3):
    set1 = set(puzzel_input[i].strip())
    set2 = set(puzzel_input[i+1].strip())
    set3 = set(puzzel_input[i+2].strip())
    sum_of_badges += Char_Value((set1 & set2 & set3).pop())

print("Part 2:",sum_of_badges)
