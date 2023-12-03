# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:21:23 2023

@author: patri
"""


# For Part2: Gear Class that lets us keep track which numbers are part of a gear.
class Gear:
    def __init__(self, y, x, partnumber):
        self.y = y
        self.x = x
        self.partnumbers = []
        self.partnumbers.append(partnumber)

    def add_partnumber(self, partnumber):
        # This is very dirty. It assumes that a gear can not have two of the same partnumbers.
        # This worked for my puzzle input but will certainly brake some inputs.
        # Well thats just is how AOC works. Right? RIGHT?!??!
        if not partnumber in self.partnumbers:
            self.partnumbers.append(partnumber)  # Method to add a new partnumber

    def get_gearratio(self):
        if len(self.partnumbers) == 2:  # Gears have exactly 2 Partnumbers
            # its a gear
            return self.partnumbers[0]*self.partnumbers[1]  # Its a gear
        else:
            return 0  # Its no gear

# For Part 2: Gearhandler Class to make it easier to handle te gear list.


class GearHandler:
    def __init__(self):
        self.gears = []
        self.index = 0

    # Iterates the gear list to add the part number or creates a neww gear when it doesnt exist.
    def add_partnumber_for_gear(self, y, x, partnumber):
        for gear in self.gears:
            if gear.y == y and gear.x == x:
                gear.add_partnumber(partnumber)
                return

        self.gears.append(Gear(y, x, partnumber))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.gears):
            result = self.gears[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


def check_if_partnumber(puzzel_input, y_coordinate: int, x_start: int, x_end: int, partnumber: int, gears_handler_list) -> bool:
    found = False
    moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    # We iterate through all the digits.
    for x_coordinate in range(x_start, x_end):
        # Checking every possible move
        for move in moves:
            try:
                value = puzzel_input[y_coordinate+move[0]][x_coordinate+move[1]]
                if value == "." or value.isdigit():
                    pass
                else:
                    # If we find a symbol then we are done. Its a part number.
                    found = True
                    if value == "*":
                        gears_handler_list.add_partnumber_for_gear(y_coordinate+move[0], x_coordinate+move[1], partnumber)
            except IndexError:
                continue
    # If we checked everything without finding a symbol we are done. No part number.
    return found


with open("input.txt", mode="r") as file:
    puzzel_input = file.readlines()

puzzel_input = [x.strip() for x in puzzel_input]
gears_handler_list = GearHandler()
list_of_numbers = []

rows = len(puzzel_input)
# since we pad the columns we add one more to the row counter.
columns = len(puzzel_input[0])+1

print(f"Rows: {rows}. Columns: {columns}")

more_number = False
y_coordinate = None
x_start = None
x_end = None
number = None

for y in range(rows):
    # To circumvent problems with numbers beeing on the end of the line we pad the grid.
    puzzel_input[y] += "."
    for x in range(columns):
        # If we find a digit
        if puzzel_input[y][x].isdigit():
            # Adding to an existing number
            if more_number:
                number += puzzel_input[y][x]
                continue
            # Found a new number
            else:
                number = puzzel_input[y][x]
                more_number = True
                x_start = x
                y_coordinate = y
                continue
        # Found no number
        else:
            # Stop building number
            if more_number:
                x_end = x
                if check_if_partnumber(puzzel_input, y, x_start, x_end, int(number), gears_handler_list):
                    list_of_numbers.append(int(number))
                    #print("Partnumber: ", number)
                else:
                    #print("Nothing:", number)
                    pass
                # TODO Check for points goes here
                more_number = False
            # Next onbe
            else:
                continue

print("Part 1: ", sum(list_of_numbers))

list_of_gearratios = []
for gear in gears_handler_list:
    list_of_gearratios.append(gear.get_gearratio())

print("Part 2: ", sum(list_of_gearratios))
