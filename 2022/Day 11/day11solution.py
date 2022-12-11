# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:53:20 2022

@author: patri
"""
import re
import math


def kleinstes_gemeinsames_vielfaches(a, b):
    ggt = math.gcd(a, b)
    kgv = (a * b) / ggt
    return int(kgv)


def monkeyBuissnes():
    biggest_monkeys = sorted(
        list_of_monkeys, key=lambda x: x.inspected, reverse=True)[:2]
    return biggest_monkeys[0].inspected * biggest_monkeys[1].inspected


class Monkey:
    def __init__(self, input_string):
        self.input_string = input_string
        self.items = re.findall(r'\d+', input_string[1])
        self.items = [int(x) for x in self.items]
        self.operation = input_string[2].split("Operation: ")[1].strip()
        self.test_divisible = int(re.findall(r'\d+', input_string[3])[0])
        self.test_true = int(re.findall(r'\d+', input_string[4])[0])
        self.test_false = int(re.findall(r'\d+', input_string[5])[0])
        self.inspected = 0

    def __str__(self):
        string = "items: " + str(self.items) + "\n"
        string += "operation: " + str(self.operation) + "\n"
        string += "test_divisible: " + str(self.test_divisible) + "\n"
        string += "test_true: " + str(self.test_true) + "\n"
        string += "test_false: " + str(self.test_false) + "\n"
        return string

    def inspect(self):
        for i, item in enumerate(self.items):
            self.inspected += 1
            if "+" in self.operation:
                self.items[i] += int(re.findall(r'\d+', self.operation)[0])
            elif "*" in self.operation:
                if re.findall(r'\d+', self.operation):
                    self.items[i] *= int(re.findall(r'\d+', self.operation)[0])
                else:
                    self.items[i] = item * item

    def throw(self, list_of_monkeys, mitigation=True):
        if mitigation:
            self.items = [int(x/3) for x in self.items]
        for item in self.items:
            if item % self.test_divisible == 0:
                list_of_monkeys[self.test_true].items.append(item % super_KGV)
            else:
                list_of_monkeys[self.test_false].items.append(item % super_KGV)
        self.items = []


with open("input.txt", "r") as f:
    puzzel_input = f.readlines()

list_of_monkeys = []

for i in range(0, len(puzzel_input), 7):
    list_of_monkeys.append(Monkey(puzzel_input[i:i+7]))

super_KGV = 19
for Monkey in list_of_monkeys:
    super_KGV = kleinstes_gemeinsames_vielfaches(
        super_KGV, int(Monkey.test_divisible))

rounds = 10000
for i in range(rounds):
    for monkey in list_of_monkeys:
        monkey.inspect()
        monkey.throw(list_of_monkeys, False)


for i in range(len(list_of_monkeys)):
    print("Monkey", i, "inspected items",
          list_of_monkeys[i].inspected, "times.")

print("Monkey Buisiness", monkeyBuissnes())
