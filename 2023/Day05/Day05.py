# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:20:30 2023

@author: patri
"""
import time


def map_value_part1(list_of_maps, value):
    for entry in list_of_maps:

        destination, source, range_length = entry.split(" ")

        value = int(value)
        destination = int(destination)
        source = int(source)
        range_length = int(range_length)

        if value >= source and value < source + range_length:
            return value + destination-source
    return value


def map_value_part2(list_of_maps, ranges):
    next_ranges = []
    leftovers = []

    for entry in list_of_maps:
        while True:
            if len(ranges) == 0:
                break
            item = ranges.pop(0)
            seed_start = item[0]
            seed_range = item[1]

            destination, source, range_length = entry.split(" ")

            destination = int(destination)
            source = int(source)
            range_length = int(range_length)

            # calculate part before

            if seed_start < source:
                leftovers.append([seed_start, min([seed_start+seed_range, source])-seed_start])
                tempholder = seed_start
                seed_start = min([seed_start+seed_range, source])
                seed_range -= (seed_start - tempholder)
            if seed_range == 0:
                continue

            if seed_range < 0:
                print("Mistakes where made")

            # calculate part inside

            if seed_start < source+range_length:
                new_range = min([source+range_length, seed_start+seed_range])-seed_start
                next_ranges.append([seed_start+destination-source, new_range])
                tempholder = seed_start
                tempholder = min([source+range_length, seed_start+seed_range])
                seed_range -= new_range
            if seed_range == 0:
                continue

            leftovers.append([seed_start, seed_range])

            if seed_range < 0:
                print("Mistakes where made")

        ranges += leftovers
        leftovers = []
    next_ranges += ranges
    return next_ranges


def calculate_destination(seeds):

    number_map = []
    for entry in puzzel_input:

        if not entry:
            new_values = []
            for seed in seeds:
                new_values.append(map_value_part1(number_map, seed))
            seeds = new_values
            new_values = []
            number_map = []
            continue
        if entry[0].isdigit():
            number_map.append(entry)
            continue
        else:
            continue
    return seeds


with open("input_limp.txt", mode="r") as file:
    puzzel_input = file.readlines()
    puzzel_input = [x.strip() for x in puzzel_input]


start_time = time.perf_counter()

# get seeds
start_seeds = puzzel_input.pop(0).split(" ")[1:]
# get rid of empty space in seeds.
puzzel_input.pop(0)
# Easier loop
puzzel_input.append("")

part1 = calculate_destination(start_seeds)

part1 = [int(x) for x in part1]
part1result = min(part1)
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Part 1: {part1result}, Runtime: {elapsed_time * 1000:.2f} ms")

part_2_seeds = []
number1 = None
number2 = None
for number in start_seeds:
    if not number1:
        number1 = int(number)
        continue
    if not number2:
        number2 = int(number)
        part_2_seeds.append([number1, number2])
        number1 = None
        number2 = None


def calculate_destination_2(seeds):

    number_map = []
    for entry in puzzel_input:

        if not entry:
            new_values = map_value_part2(number_map, seeds)

            limpvalues = [[x[0], x[0]+x[1]] for x in new_values]
            seeds = new_values
            new_values = []
            number_map = []
            continue
        if entry[0].isdigit():
            number_map.append(entry)
            continue
        else:
            continue
    return seeds


start_time = time.perf_counter()
part2 = calculate_destination_2(part_2_seeds)
minrange = [x[0] for x in part2]
part2_result = min(minrange)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 2: {part2_result}, Runtime: {elapsed_time * 1000:.2f} ms")

# part2 = [int(x) for x in part1]
# part1result = min(part1)


# print(map_value_part2(list_of_maps, ranges))
