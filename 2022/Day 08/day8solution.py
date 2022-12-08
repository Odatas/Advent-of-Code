# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 07:52:14 2022

@author: pphilipiak
"""


with open("input.txt", "r") as f:
    puzzel_input = f.readlines()

puzzel_input = [x.strip() for x in puzzel_input]

visible_trees = 0
max_scenic_score = 1


for y in range(len(puzzel_input)):
    for x in range(len(puzzel_input[y])):
        current_tree_height = int(puzzel_input[y][x])
        counted = False
        scenic_score = 1
        # If tree at edge
        if x == 0 or y == 0 or x == len(puzzel_input[y])-1 or y == len(puzzel_input)-1:
            visible_trees += 1
            counted = True
            scenic_score = 0

        # check Top
        for y_counter in reversed(range(y)):
            if int(puzzel_input[y_counter][x]) >= current_tree_height:
                scenic_score *= y-y_counter
                break
            if y_counter == 0:
                scenic_score *= y-y_counter
                if not counted:
                    visible_trees += 1
                    counted = True

        # check bottom
        for y_counter in range(y+1, len(puzzel_input)):
            if int(puzzel_input[y_counter][x]) >= current_tree_height:
                scenic_score *= y_counter-y
                break
            if y_counter == len(puzzel_input)-1:
                scenic_score *= y_counter-y
                if not counted:
                    visible_trees += 1
                    counted = True

        # check left
        for x_counter in reversed(range(x)):
            if int(puzzel_input[y][x_counter]) >= current_tree_height:
                scenic_score *= x - x_counter
                break
            if x_counter == 0:
                scenic_score *= x - x_counter
                if not counted:
                    visible_trees += 1
                    counted = True

        # check right
        for x_counter in range(x+1, len(puzzel_input[y])):
            if int(puzzel_input[y][x_counter]) >= current_tree_height:
                scenic_score *= x_counter - x
                break
            if x_counter == len(puzzel_input[y])-1:
                scenic_score *= x_counter - x
                if not counted:
                    visible_trees += 1
                    counted = True

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score


print("Part 1:", visible_trees)
print("Part 2:", max_scenic_score)
