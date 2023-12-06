# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:11:53 2023

@author: patri
"""


def ways_to_win(racetime, record):

    distance = 0
    speed = 0
    winnings = 0

    for holding_time in range(racetime):
        distance = holding_time * (racetime-holding_time)
        if distance > record:
            winnings += 1

    return winnings


print("Part 1: ", ways_to_win(46, 347) * ways_to_win(82, 1522) * ways_to_win(84, 1406) * ways_to_win(79, 1471))

print("Part 2: ", ways_to_win(46828479, 347152214061471))
