# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 07:49:02 2023

@author: patri
"""

import time


def calculate_all_extrapolations(list_to_interpolate):
    list_to_interpolate[len(list_to_interpolate)-1].append(0)
    for index in reversed(range(len(list_to_interpolate)-1)):
        list_to_interpolate[index].append(list_to_interpolate[index][-1]+list_to_interpolate[index+1][-1])
    return list_to_interpolate


def calculate_extrapolation_value(list_of_values):
    difference_list = []
    difference_list.append(list_of_values)
    while True:
        new_difference_entry = []
        previous_entry = difference_list[len(difference_list)-1]
        for index in range(len(previous_entry)-1):
            new_difference_entry.append(previous_entry[index+1] - previous_entry[index])
        difference_list.append(new_difference_entry)

        if all(element == 0 for element in new_difference_entry):
            difference_list = calculate_all_extrapolations(difference_list)
            return difference_list[0][-1]


with open("input.txt", mode="r") as file:
    puzzle_input = file.readlines()
    puzzle_input = [[int(y) for y in x.strip().split(" ")] for x in puzzle_input]

start_time = time.perf_counter()
part1result = 0
for i in puzzle_input:
    # print(i)
    solution = calculate_extrapolation_value(i.copy())
    part1result += solution
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 1: {part1result}, Runtime: {elapsed_time * 1000:.2f} ms")

start_time = time.perf_counter()
part2result = 0
for i in puzzle_input:
    # Reverse every puzzel_input before calculating the rest.
    solution = calculate_extrapolation_value(i[::-1])
    part2result += solution
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 2: {part2result}, Runtime: {elapsed_time * 1000:.2f} ms")
