# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 07:55:31 2023

@author: patri
"""

import re

with open("input.txt", mode="r") as file:
    puzzelinput = file.readlines()


possiblegames = []
powerofcubes = []

# ammount of cubes
redcubes = 12
greencubes = 13
bluecubes = 14


for game in puzzelinput:
    # get gameid
    gameid = game.split(":")[0].split(" ")[1]

    # Extract cube numbers
    green_numbers = re.findall(r'(\d+) green', game)
    blue_numbers = re.findall(r'(\d+) blue', game)
    red_numbers = re.findall(r'(\d+) red', game)

    # Convert number strings to integers
    green_numbers_int = [int(num) for num in green_numbers]
    blue_numbers_int = [int(num) for num in blue_numbers]
    red_numbers_int = [int(num) for num in red_numbers]

    fewest_green = max(green_numbers_int)
    fewest_red = max(red_numbers_int)
    fewest_blue = max(blue_numbers_int)
    powerofcubes.append(fewest_red*fewest_green*fewest_blue)

    # Check if all numbers are smaller or equal to respective cube limits
    all_green_smaller_or_equal = all(num <= greencubes for num in green_numbers_int)
    all_blue_smaller_or_equal = all(num <= bluecubes for num in blue_numbers_int)
    all_red_smaller_or_equal = all(num <= redcubes for num in red_numbers_int)

    if all_green_smaller_or_equal and all_blue_smaller_or_equal and all_red_smaller_or_equal:
        possiblegames.append(int(gameid))

print("Part 1: ", sum(possiblegames))
print("Part 2: ", sum(powerofcubes))
