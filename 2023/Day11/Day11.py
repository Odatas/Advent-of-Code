# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:37:40 2023

@author: patri
"""


def count_between(numbers, A, B):
    # Determine the smaller and larger of the two numbers
    if A == B:
        return 0
    smaller = min(A, B)
    larger = max(A, B)

    # Count the numbers in the specified range
    count = 0
    for num in numbers:
        if smaller <= num <= larger:
            count += 1

    return count


def calulate_shortes_path_with_expansion(expansionfactor):

    with open("input.txt", mode="r") as file:
        puzzel_input = file.readlines()
        puzzel_input = [x.strip() for x in puzzel_input]

    empty_rows = []
    empty_collumns = []

    empty_row = '.' * int(len(puzzel_input[0]))
    for row in range(len(puzzel_input)):
        if puzzel_input[row] == empty_row:
            empty_rows.append(row)

    column_index = 0
    empty_column = '.' * int(len(puzzel_input))
    while column_index < len(puzzel_input[0]):
        column = "".join([s[column_index] for s in puzzel_input])
        if empty_column == column:
            empty_collumns.append(column_index)
        column_index += 1

    galaxie_list = []
    for column in range(len(puzzel_input[0])):
        for row in range(len(puzzel_input)):
            if puzzel_input[row][column] == "#":
                galaxie_list.append([row, column])

    combined_sum = 0
    while True:
        if galaxie_list:
            current_galaxy = galaxie_list.pop(0)
            for galaxy in galaxie_list:

                shortest_path_y = abs(galaxy[0]-current_galaxy[0]) + count_between(empty_rows, galaxy[0], current_galaxy[0]
                                                                                   ) * expansionfactor - count_between(empty_rows, galaxy[0], current_galaxy[0])
                shortes_path_x = abs(galaxy[1]-current_galaxy[1]) + count_between(empty_collumns, galaxy[1], current_galaxy[1]
                                                                                  ) * expansionfactor - count_between(empty_collumns, galaxy[1], current_galaxy[1])
                shortest_path_combined = shortes_path_x + shortest_path_y
                combined_sum += shortest_path_combined
        else:
            break
    return combined_sum


part1 = calulate_shortes_path_with_expansion(2)
print("Part 1: ", part1)

part2 = calulate_shortes_path_with_expansion(1000000)
print("Part 2: ", part2)
