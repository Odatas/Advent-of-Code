# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:01:57 2023

@author: patri
"""


with open("input.txt", mode="r") as file:
    puzzelinput = file.readlines()


numbers = []

for row in puzzelinput:
    firstnumber = None
    lastnumber = None
    for char in row:
        if char.isdigit():
            if firstnumber:
                lastnumber = char
            else:
                firstnumber = char
    if not lastnumber:
        lastnumber = firstnumber
    print(row)
    if firstnumber and lastnumber:
        numbers.append(int(firstnumber+lastnumber))

print("Part 1:", sum(numbers))

numbers = []

numbermap = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine",
    "zero": "z0ero"
}


for row in puzzelinput:
    newstring = row
    for word, number in numbermap.items():
        newstring = newstring.replace(word, number)
    print(row, newstring)
    firstnumber = None
    lastnumber = None
    for char in newstring:
        if char.isdigit():
            if firstnumber:
                lastnumber = char
            else:
                firstnumber = char
    if not lastnumber:
        lastnumber = firstnumber
    print(firstnumber, lastnumber)
    numbers.append(int(firstnumber+lastnumber))

print("Part 2:", sum(numbers))
