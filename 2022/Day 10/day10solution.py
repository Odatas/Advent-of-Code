# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:09:52 2022

@author: patri
"""


def changeCycle(cycle):

    if x_register-1 == cycle % 40 or x_register == cycle % 40 or x_register + 1 == cycle % 40:
        crt_screen.append("#")
    else:
        crt_screen.append(".")
    cycle += 1
    important_cycles = [20, 60, 100, 140, 180, 220]
    if cycle in important_cycles:
        important_cycle_values.append(x_register*cycle)
    return cycle


with open("input.txt", "r") as f:
    puzzel_input = f.readlines()

puzzel_input = [x.strip() for x in puzzel_input]
crt_screen = []
cycle = 0
x_register = 1
important_cycle_values = []
for i in puzzel_input:
    if "noop" in i:
        cycle = changeCycle(cycle)
        continue
    else:
        for j in range(2):
            cycle = changeCycle(cycle)
        print(x_register)
        x_register += int(i.split(" ")[1])

print("Part 1:", sum(important_cycle_values))

print("Part 2:")

for i in range(0, 240, 40):
    print("".join(crt_screen[i:i+40]))
