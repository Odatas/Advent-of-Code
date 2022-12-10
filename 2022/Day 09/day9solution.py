# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 07:56:47 2022

@author: pphilipiak
"""


def Save_Coordinates(x, y):
    if not (x, y) in visited_coordinates:
        visited_coordinates.append((x, y))
        return True
    return False


def Get_Difference(head, tail):
    return (head["x"]-tail["x"], head["y"]-tail["y"])


with open("input.txt", "r") as f:
    puzzel_input = f.readlines()

puzzel_input = [x.strip() for x in puzzel_input]
visited_coordinates = []
head = {"x": 0, "y": 0}
Save_Coordinates(0, 0)
dont_move_list = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]

rope_length = 9
rope = []
rope.append(head)
for i in range(rope_length):
    rope.append({"x": 0, "y": 0})

# pro Instruktion
for i in puzzel_input:
    # pro schritt in instruktion
    for j in range(int(i.split(" ")[1])):
        # for ever part of the rope
        for knot in range(len(rope)):
            if rope[knot] is head:
                # Move head
                if i[0] == "U":
                    rope[knot]["y"] += 1
                if i[0] == "D":
                    rope[knot]["y"] -= 1
                if i[0] == "R":
                    rope[knot]["x"] += 1
                if i[0] == "L":
                    rope[knot]["x"] -= 1
            else:
                # knot touches nod ahead
                if Get_Difference(rope[knot-1], rope[knot]) in dont_move_list:
                    pass
                # knot in line with knot ahead
                elif Get_Difference(rope[knot-1], rope[knot])[0] == 0:
                    if Get_Difference(rope[knot-1], rope[knot])[1] > 0:
                        rope[knot]["y"] += 1
                    else:
                        rope[knot]["y"] -= 1
                elif Get_Difference(rope[knot-1], rope[knot])[1] == 0:
                    if Get_Difference(rope[knot-1], rope[knot])[0] > 0:
                        rope[knot]["x"] += 1
                    else:
                        rope[knot]["x"] -= 1
                # knot not in line with rope ahead
                else:
                    if Get_Difference(rope[knot-1], rope[knot])[1] > 0:
                        rope[knot]["y"] += 1
                    else:
                        rope[knot]["y"] -= 1
                    if Get_Difference(rope[knot-1], rope[knot])[0] > 0:
                        rope[knot]["x"] += 1
                    else:
                        rope[knot]["x"] -= 1
                # if its the end then save coordinates
                if rope[knot] is rope[-1]:
                    Save_Coordinates(rope[knot]["x"], rope[knot]["y"])

print("Part 1:", len(visited_coordinates))
