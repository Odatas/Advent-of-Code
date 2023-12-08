# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:48:11 2023

@author: patri
"""

import re
import time
from math import lcm


def find_step_count(starting_node, part2=False):
    current_place = starting_node
    step_counter = 0
    while True:
        for step in steps:
            if step == "L":
                current_place = map_dict[current_place][0]
            else:
                current_place = map_dict[current_place][1]
            step_counter += 1
            if part2:
                if current_place[2] == "Z":
                    return step_counter
            else:
                if current_place == "ZZZ":
                    return step_counter


with open("input.txt", mode="r") as file:
    puzzel_input = file.readlines()
puzzel_input = [x.strip() for x in puzzel_input]


steps = puzzel_input.pop(0)
puzzel_input.pop(0)


map_dict = {}
pattern = r"([A-Za-z0-9]{3})"
part2_start = []
for entry in puzzel_input:
    matches = re.findall(pattern, entry)
    map_dict[matches[0]] = (matches[1], matches[2])
    if matches[0][2] == "A":
        part2_start.append(matches[0])

start_time = time.perf_counter()
part1result = find_step_count("AAA")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 1: {part1result}, Runtime: {elapsed_time * 1000:.2f} ms")

start_time = time.perf_counter()
step_counter = [find_step_count(x, True) for x in part2_start]
part2result = lcm(*step_counter)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 2: {part2result}, Runtime: {elapsed_time * 1000:.2f} ms")
