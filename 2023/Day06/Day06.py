# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:11:53 2023

@author: patri
"""
import time


def ways_to_win(racetime, record):

    distance = 0
    speed = 0
    winnings = 0
    counter = 0

    for holding_time in range(racetime):
        counter += 1
        distance = holding_time * (racetime-holding_time)
        if distance > record:
            winnings += 1

    return winnings


start_time = time.perf_counter()
part1result = ways_to_win(46, 347) * ways_to_win(82, 1522) * ways_to_win(84, 1406) * ways_to_win(79, 1471)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Part 1: {part1result}, Runtime: {elapsed_time * 1000:.2f} ms")


start_time = time.perf_counter()
part2result = ways_to_win(46828479, 347152214061471)
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Part 2: {part2result}, Runtime: {elapsed_time * 1000:.2f} ms")
