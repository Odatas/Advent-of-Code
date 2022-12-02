# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:05:11 2021

@author: Spongetheone
"""

with open(r'''day3.txt''') as f:
    lines = f.readlines()

with open(r'''day3.txt''') as f:
    highlist = f.readlines()

with open(r'''day3.txt''') as f:
    lowlist = f.readlines()


#part1
high=""
low=""

for i in range(len(lines[0])-1):
    ones = 0
    zeros = 0
    for j in lines:
        if j[i] == "0":
            zeros +=1
        elif j[i] == "1":
            ones +=1
        else:
            print("Something stinks")

    if zeros > ones:
        high = high + "0"
        low = low + "1"
    else:
        high = high +  "1"
        low = low + "0"


print("Part 1:",int(high,2) * int(low,2))

high=0
low=0
for i in range(len(highlist[0])-1):
    ones = 0
    zeros = 0
    for j in highlist:
        if j[i] == "0":
            zeros +=1
        elif j[i] == "1":
            ones +=1
        else:
            print("Something stinks")

    if zeros > ones:
        highlist = [x for x in highlist if x[i] == "0"]
    else:
        highlist = [x for x in highlist if x[i] == "1"]
    if(len(highlist)==1):
        high =int(highlist[0],2)
        break


for i in range(len(lowlist[0])-1):
    ones = 0
    zeros = 0
    for j in lowlist:
        if j[i] == "0":
            zeros +=1
        elif j[i] == "1":
            ones +=1
        else:
            print("Something stinks")

    if zeros > ones:
        lowlist = [x for x in lowlist if x[i] == "1"]
    else:
        lowlist = [x for x in lowlist if x[i] == "0"]
    if(len(lowlist)==1):
        low=int(lowlist[0],2)
        break

print("Part 2:", high*low)

