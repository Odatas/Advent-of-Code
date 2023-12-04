# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:48:35 2023

@author: patri
"""

import re


with open("input.txt", mode="r") as file:
    puzzel_input = file.readlines()

cardcount = len(puzzel_input)
scratchcard_points = []
carddeck_winnings_per_card = []


for card in puzzel_input:

    # Pattern for numbers between ":" and "|"
    our_numbers = re.search(r':\s*((?:\d+\s*)+)\|', card)
    our_numbers = our_numbers.group(1).split() if our_numbers else []

    # Pattern for numbers after "|"
    winning_numbers = re.search(r'\|\s*(\d[\d\s]*)', card)
    winning_numbers = winning_numbers.group(1).split() if winning_numbers else []

    winner = -1

    for number in our_numbers:
        if number in winning_numbers:
            winner += 1
    if winner >= 0:
        carddeck_winnings_per_card.append(winner+1)
        scratchcard_points.append(2 ** winner)
    else:
        carddeck_winnings_per_card.append(0)

print("Part 1: ", sum(scratchcard_points))

carddeck_total_counts = []
carddeck_current_round_counter = []
carddeck_next_round_counter = []
winner_found = True

for i in range(cardcount):
    carddeck_total_counts.append(1)
    carddeck_current_round_counter.append(1)
    carddeck_next_round_counter.append(0)


while True:
    for i in range(cardcount):
        adding = carddeck_winnings_per_card[i]

        for j in range(1, adding+1):
            carddeck_next_round_counter[i+j] += carddeck_current_round_counter[i]

    if sum(carddeck_next_round_counter) == 0:
        break
    for i in range(cardcount):
        carddeck_total_counts[i] += carddeck_next_round_counter[i]
    carddeck_current_round_counter = carddeck_next_round_counter
    carddeck_next_round_counter = []
    for i in range(cardcount):
        carddeck_next_round_counter.append(0)

print("Part 2: ", sum(carddeck_total_counts))
