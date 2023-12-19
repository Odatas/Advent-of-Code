# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 07:21:44 2023

@author: patri
"""

import time


# coordinates[y,x]
# Top Left ist 0,0 and y is positiv south and x is positive east

# north = [-1,0]
# south = [1,0]
# west  = [0,-1]
# east  = [0,1]


step_map = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    ".": None
}


def find_enclosed_areas(grid):
    counter = 0
    inside = False
    for y in range(len(grid)):
        inside = False
        for x in range(len(grid[0])):
            if y < len(grid)-1:
                if grid[y][x] + 1 == grid[y+1][x]:
                    # down
                    #grid[y][x] = -1
                    inside = True
                    continue
                elif grid[y][x] - 1 == grid[y+1][x]:
                    # up
                    #grid[y][x] = -2
                    inside = False
                    continue
                elif grid[y][x] == 0 and inside:
                    counter += 1
                    grid[y][x] = "I"
    return counter


def calculate_step_count(current_position, previous_position, floodfill_grid):
    step_counter = 0
    pos_current = current_position.copy()
    pos_previous = previous_position.copy()
    step_number = 0
    while True:
        temp_position = pos_current.copy()
        if grid[pos_current[0]][pos_current[1]] == "S":
            # print("Steps Until S: ", step_counter)
            return step_counter
        if grid[pos_current[0]][pos_current[1]] == ".":
            return 0
        try:
            steps = step_map[grid[pos_current[0]][pos_current[1]]]
        except KeyError:
            print("This should not show up")
            return step_counter
        possibble_next_position = [pos_current[0]+steps[0][0], pos_current[1]+steps[0][1]]
        if possibble_next_position == pos_previous:
            pos_current[0] += steps[1][0]
            pos_current[1] += steps[1][1]

        else:
            pos_current[0] += steps[0][0]
            pos_current[1] += steps[0][1]
        floodfill_grid[pos_current[0]][pos_current[1]] = step_number
        step_number += 1
        pos_previous = temp_position
        step_counter += 1
        # print("Current: ", pos_current, "Previous: ", pos_previous)
        continue


with open("input.txt", mode="r") as file:
    grid = file.readlines()
    grid = [list(x.strip()) for x in grid]

num_rows = len(grid)
num_cols = len(grid[0]) if num_rows > 0 else 0

# Create a new grid filled with zeros
grid_path1 = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
grid_path2 = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
grid_path3 = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
grid_path4 = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

start_time = time.perf_counter()

position = [0, 0]
found = False
for index_y, line in enumerate(grid):
    for index_x, value in enumerate(line):
        if value == "S":
            position = [index_y, index_x]
            found = True
            break
    if found:
        break
previous_position = position.copy()
final_path = 0
final_grid = None


current_position = [position[0], position[1]+1]
path1 = calculate_step_count(current_position, previous_position, grid_path1)

if path1 > final_path:
    final_path = path1
    final_grid = grid_path1


current_position = [position[0], position[1]-1]
path2 = calculate_step_count(current_position, previous_position, grid_path2)

if path2 > final_path:
    final_path = path2
    final_grid = grid_path2

current_position = [position[0]+1, position[1]]
path3 = calculate_step_count(current_position, previous_position, grid_path3)

if path3 > final_path:
    final_path = path3
    final_grid = grid_path3

current_position = [position[0]-1, position[1]]
path4 = calculate_step_count(current_position, previous_position, grid_path4)

if path4 > final_path:
    final_path = path4
    final_grid = grid_path4

end_time = time.perf_counter()
elapsed_time = end_time - start_time
# I count + 1 to account for odd numbers. If im allready at an even number the division will take care
print(f"Part 1: {(final_path+1)/2}, Runtime: {elapsed_time * 1000:.2f} ms")

start_time = time.perf_counter()
enclosed_area = find_enclosed_areas(final_grid)


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 2: {enclosed_area}, Runtime: {elapsed_time * 1000:.2f} ms")
