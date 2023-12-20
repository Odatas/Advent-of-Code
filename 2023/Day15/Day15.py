# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:48:15 2023

@author: patri
"""


def hash_algo(value):
    new_value = 0
    for char in value:
        new_value += ord(char)
        new_value = new_value * 17
        new_value = new_value % 256
    return new_value


with open("input.txt", mode="r") as file:
    puzzel_input = file.readline()
    puzzel_input = puzzel_input.split(",")
    puzzel_input = [x.strip() for x in puzzel_input]


part_1_sum = []
for value in puzzel_input:
    part_1_sum.append(hash_algo(value))


print("Part 1: ", sum(part_1_sum))

hashmap = {}


for i in puzzel_input:
    for index in range(len(i)):
        if i[index] == "-" or i[index] == "=":
            label_alphas = i[:index]
    box_value = hash_algo(label_alphas)
    if "=" in i:
        label = label_alphas + " " + i[-1]
        if box_value in hashmap:
            box_content = hashmap[box_value]
            found = False
            for index in range(len(box_content)):
                if label_alphas in box_content[index]:
                    box_content[index] = label
                    found = True
                    break
            if not found:
                box_content.append(label)
        else:
            hashmap[box_value] = [label]
    elif "-" in i:
        if box_value in hashmap:
            box_content = hashmap[box_value]
            for index in range(len(box_content)):
                if label_alphas in box_content[index]:
                    box_content.pop(index)
                    break
part_2_sum = []
for key in hashmap:

    for index in range(len(hashmap[key])):
        if len(hashmap[key]) > 1:
            print(hashmap[key], hashmap[key][index])
        aaa_box = key+1
        aa_slot = index+1
        a_focal_length = int(hashmap[key][index][-1])
        value = aaa_box * aa_slot * a_focal_length
        part_2_sum.append(value)

print("Part 2: ", sum(part_2_sum))
